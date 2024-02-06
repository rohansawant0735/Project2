import psutil
import logging

# Set the thresholds for monitoring
cpu_threshold = 50.0
memory_threshold = 45.0
disk_threshold = 50.0

# Configure logging to a file
logging.basicConfig(filename='system_health.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def check_system_health():
    # Get system metricsS
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    processes = psutil.process_iter()

    # Check CPU usage
    if cpu_usage > cpu_threshold:
        logging.warning(f"High CPU usage detected: {cpu_usage}%")

    # Check memory usage
    if memory_usage > memory_threshold:
        logging.warning(f"High memory usage detected: {memory_usage}%")

    # Check disk space
    if disk_usage > disk_threshold:
        logging.warning(f"Low disk space detected: {disk_usage}%")

    # Check running processes
    for process in processes:
        if process.cpu_percent() > cpu_threshold:
            logging.warning(f"High CPU usage for process {process.name()} ({process.pid}): {process.cpu_percent()}%")

# Run the system health check
check_system_health()
