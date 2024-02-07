import psutil
import logging

cpu_threshold = 50.0
memory_threshold = 45.0
disk_threshold = 50.0

logging.basicConfig(filename='system_health.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def check_system_health():
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    processes = psutil.process_iter()

    if cpu_usage > cpu_threshold:
        logging.warning(f"High CPU usage detected: {cpu_usage}%")

    if memory_usage > memory_threshold:
        logging.warning(f"High memory usage detected: {memory_usage}%")

    if disk_usage > disk_threshold:
        logging.warning(f"Low disk space detected: {disk_usage}%")

    for process in processes:
        if process.cpu_percent() > cpu_threshold:
            logging.warning(f"High CPU usage for process {process.name()} ({process.pid}): {process.cpu_percent()}%")

check_system_health()
