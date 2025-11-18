import logging
import requests
import os
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
import atexit

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TARGET_URL = "https://caemanagement.onrender.com/marketplace"

_scheduler_started = False

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

def start_scheduler():
    """
    Initialize and start the background scheduler.
    This should be called once when the application starts.
    
    Guards against duplicate starts in multi-process environments (Gunicorn with --reload).
    Only starts in the actual worker process, not in the reloader parent process.
    """
    global _scheduler_started
    
    if _scheduler_started:
        logger.info("Scheduler already started in this process, skipping duplicate start")
        return None
    
    if os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
        logger.info("Detected Flask development reloader parent process, skipping scheduler")
        return None
    
    gunicorn_worker_id = os.environ.get('GUNICORN_WORKER_ID')
    if gunicorn_worker_id and gunicorn_worker_id != '0':
        logger.info(f"Detected Gunicorn worker {gunicorn_worker_id}, scheduler only runs in worker 0")
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
        
        atexit.register(lambda: scheduler.shutdown())
        
        return scheduler
        
    except Exception as e:
        logger.error(f"Failed to start scheduler: {e}")
        return None
