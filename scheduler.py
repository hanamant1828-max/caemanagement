import logging
import requests
import os
import fcntl
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
import atexit

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TARGET_URL = "https://caemanagement.onrender.com/marketplace"

_scheduler_started = False
_lock_file = None

def call_external_url():
    """
    Scheduled task that calls the external URL every 5 minutes.
    This keeps the external service active and prevents cold starts.
    """
    try:
        logger.info(f"[{datetime.now()}] Calling external URL: {TARGET_URL}")
        
        response = requests.get(TARGET_URL, timeout=30)
        
        if response.status_code == 200:
            logger.info(f"Successfully called {TARGET_URL} - Status: {response.status_code}")
        else:
            logger.warning(f"Call to {TARGET_URL} returned status: {response.status_code}")
            
    except requests.exceptions.Timeout:
        logger.error(f"Timeout while calling {TARGET_URL}")
    except requests.exceptions.RequestException as e:
        logger.error(f"Error calling {TARGET_URL}: {str(e)}")
    except Exception as e:
        logger.error(f"Unexpected error in scheduled task: {str(e)}")

def acquire_scheduler_lock():
    """
    Acquire an exclusive file lock to ensure only one scheduler runs across all processes.
    Returns the lock file handle if successful, None otherwise.
    """
    global _lock_file
    lock_path = '/tmp/scheduler.lock'
    
    try:
        _lock_file = open(lock_path, 'w')
        fcntl.flock(_lock_file.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        _lock_file.write(str(os.getpid()))
        _lock_file.flush()
        logger.info(f"Successfully acquired scheduler lock (PID: {os.getpid()})")
        return _lock_file
    except IOError:
        logger.info(f"Another process already holds the scheduler lock, skipping scheduler start")
        if _lock_file:
            _lock_file.close()
            _lock_file = None
        return None
    except Exception as e:
        logger.error(f"Error acquiring scheduler lock: {e}")
        if _lock_file:
            _lock_file.close()
            _lock_file = None
        return None

def release_scheduler_lock():
    """Release the scheduler lock file."""
    global _lock_file
    if _lock_file:
        try:
            fcntl.flock(_lock_file.fileno(), fcntl.LOCK_UN)
            _lock_file.close()
            _lock_file = None
            logger.info("Released scheduler lock")
        except Exception as e:
            logger.error(f"Error releasing scheduler lock: {e}")

def start_scheduler():
    """
    Initialize and start the background scheduler.
    Uses file-based locking to ensure only one scheduler runs across all processes.
    
    This is safe for multi-process environments like Gunicorn with multiple workers.
    """
    global _scheduler_started
    
    if _scheduler_started:
        logger.info("Scheduler already started in this process, skipping duplicate start")
        return None
    
    lock = acquire_scheduler_lock()
    if not lock:
        return None
    
    try:
        scheduler = BackgroundScheduler()
        
        scheduler.add_job(
            func=call_external_url,
            trigger="interval",
            minutes=5,
            id='call_external_url',
            name='Call external URL every 5 minutes',
            replace_existing=True
        )
        
        scheduler.start()
        _scheduler_started = True
        logger.info("✓ Scheduler started successfully - will call external URL every 5 minutes")
        
        atexit.register(lambda: (scheduler.shutdown(), release_scheduler_lock()))
        
        return scheduler
        
    except Exception as e:
        logger.error(f"Failed to start scheduler: {e}")
        release_scheduler_lock()
        return None
