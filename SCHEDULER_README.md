# Background Scheduler Documentation

## Overview

This application includes a background scheduler that automatically calls an external URL every 5 minutes. This functionality is useful for keeping external services active and preventing cold starts on hosting platforms like Render.

## How It Works

### Scheduler Implementation

The scheduler is implemented using **APScheduler** (Advanced Python Scheduler) with the following features:

- **File-based locking**: Ensures only ONE scheduler instance runs across all processes
- **Multi-process safe**: Works correctly with Gunicorn workers and reload mode
- **Automatic error handling**: Logs errors and continues running
- **Graceful shutdown**: Properly cleans up resources on application exit

### Files

- `scheduler.py` - Contains the scheduler implementation
- `app.py` - Initializes the scheduler on application startup

### Configuration

**Target URL**: `https://caemanagement.onrender.com/marketplace`
**Interval**: Every 5 minutes
**Timeout**: 30 seconds per request

### Key Features

1. **File-based Lock Mechanism**
   - Uses `/tmp/scheduler.lock` to coordinate across processes
   - Only the first process to acquire the lock starts the scheduler
   - Other processes skip scheduler initialization

2. **Robust Error Handling**
   - Handles network timeouts gracefully
   - Logs all errors for debugging
   - Continues running even if individual requests fail

3. **Production Ready**
   - Works with Gunicorn's `--reload` flag
   - Safe for multi-worker configurations
   - Automatically releases lock on shutdown

## Monitoring

### Check Scheduler Status

The scheduler logs important events:

```
INFO:scheduler:Successfully acquired scheduler lock (PID: 2977)
INFO:scheduler:✓ Scheduler started successfully - will call external URL every 5 minutes
INFO:scheduler:[2025-11-18 11:17:59] Calling external URL: https://caemanagement.onrender.com/marketplace
INFO:scheduler:Successfully called https://caemanagement.onrender.com/marketplace - Status: 200
```

### View Logs

Check the application logs to see scheduler activity:
- Startup messages confirm the scheduler is running
- Each URL call is logged with timestamp and status
- Errors are logged with details for troubleshooting

## Customization

### Change the URL

Edit `scheduler.py` and modify the `TARGET_URL` variable:

```python
TARGET_URL = "https://your-url-here.com/endpoint"
```

### Change the Interval

Edit the `start_scheduler()` function in `scheduler.py`:

```python
scheduler.add_job(
    func=call_external_url,
    trigger="interval",
    minutes=5,  # Change this value
    ...
)
```

Available time units:
- `seconds=30` - Every 30 seconds
- `minutes=5` - Every 5 minutes
- `hours=1` - Every hour
- `days=1` - Every day

### Disable the Scheduler

To disable the scheduler, comment out or remove these lines from `app.py`:

```python
# try:
#     from scheduler import start_scheduler
#     start_scheduler()
#     logging.info("Background scheduler started successfully")
# except Exception as e:
#     logging.error(f"Failed to start scheduler: {e}")
```

## Troubleshooting

### Scheduler Not Starting

Check logs for:
```
INFO:scheduler:Another process already holds the scheduler lock
```
This is normal - it means another process already started the scheduler.

### Network Errors

```
ERROR:scheduler:Error calling https://... : [error details]
```
- Check your internet connection
- Verify the target URL is accessible
- Check for firewall restrictions

### Multiple Requests

If you see duplicate scheduler starts:
- Ensure file locking is working (`/tmp/scheduler.lock` should exist)
- Check that only one process shows "Successfully acquired scheduler lock"
- Verify Gunicorn worker count (`gunicorn --workers=1` recommended)

## Dependencies

- `APScheduler` - For scheduling background tasks
- `requests` - For making HTTP calls
- `fcntl` - For file-based locking (Unix/Linux systems)

These are automatically installed via `requirements.txt`.
