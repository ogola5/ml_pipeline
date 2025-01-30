import os
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define paths
data_raw = "data/raw"
data_processed = "data/processed"
scripts = "scripts"

# Define processing functions
def process_new_file(file_path):
    logging.info(f"Processing new file: {file_path}")
    os.system(f"python {scripts}/upload_and_convert.py {file_path}")
    os.system(f"python {scripts}/clean_data.py")
    os.system(f"python {scripts}/train_model.py")
    os.system(f"python {scripts}/retrain_model.py")
    logging.info("Pipeline completed for the new file.")

# Monitor directory manually instead of using watchdog
def monitor_directory():
    processed_files = set()
    while True:
        try:
            files = set(os.listdir(data_raw))
            new_files = files - processed_files
            for file in new_files:
                file_path = os.path.join(data_raw, file)
                if os.path.isfile(file_path):
                    process_new_file(file_path)
                    processed_files.add(file)
            time.sleep(10)
        except KeyboardInterrupt:
            logging.info("Automation stopped.")
            break
        except Exception as e:
            logging.error(f"Error occurred: {e}")

if __name__ == "__main__":
    logging.info("Starting automated pipeline...")
    monitor_directory()
