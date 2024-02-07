import shutil
import logging

# source_directory
source_directory = r'C:\Users\ROHAN\PycharmProjects\Project2.py\Project2.py'

# destination_directory
destination_directory = r'C:\Users\ROHAN\PycharmProjects\Project2.py\Backup'

logging.basicConfig(filename='backup.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def backup_directory():
    try:
        shutil.copytree(source_directory, destination_directory)

        logging.info("Backup successful: Directory copied to destination.")
    except Exception as e:
        logging.error(f"Backup failed: {str(e)}")

backup_directory()
