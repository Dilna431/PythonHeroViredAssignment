import os
import shutil
import sys
from datetime import datetime

def backup_files(source_dir, dest_dir):

    try:
        # Check if source directory exists
        if not os.path.exists(source_dir):
            print(f"Error: Source directory '{source_dir}' does not exist.")
            return
        
        # Check if destination directory exists; if not, create it
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        # Iterate through files in the source directory
        for file_name in os.listdir(source_dir):
            source_file_path = os.path.join(source_dir, file_name)
            
            # Skip directories, process only files
            if os.path.isfile(source_file_path):
                dest_file_path = os.path.join(dest_dir, file_name)
                
                # If a file with the same name exists in the destination, append a timestamp
                if os.path.exists(dest_file_path):
                    timestamp = datetime.now().strftime("%Y%m%d")
                    base_name, ext = os.path.splitext(file_name)
                    new_file_name = f"{base_name}_{timestamp}{ext}"
                    dest_file_path = os.path.join(dest_dir, new_file_name)
                
                # Copy file to the destination directory
                shutil.copy2(source_file_path, dest_file_path)
                print(f"Copied: {file_name} -> {dest_file_path}")

        print("Backup completed successfully.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    
    source_dir = sys.argv[1]
    dest_dir = sys.argv[2]
    backup_files(source_dir, dest_dir)
