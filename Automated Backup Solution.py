import shutil
import logging

# Modify the source_directory for your system using a raw string
source_directory = r'C:\Users\ROHAN\PycharmProjects\Project2.py\Project2.py'

# Modify the destination_directory for your backup location using a raw string
destination_directory = r'C:\Users\ROHAN\PycharmProjects\Project2.py\Backup'

# Configure logging to a file
logging.basicConfig(filename='backup.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def backup_directory():
    try:
        # Perform backup using shutil
        shutil.copytree(source_directory, destination_directory)

        # Check the success and log
        logging.info("Backup successful: Directory copied to destination.")
    except Exception as e:
        # Log the failure
        logging.error(f"Backup failed: {str(e)}")

# Run the backup process
backup_directory()
