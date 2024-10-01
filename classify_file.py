import os
import shutil

extension_types = {
    'images': ['jpg', 'png', 'webp'],
    'documents': ['pdf', 'docx', 'xlsx', 'csv', 'txt'],
    'archives': ['zip', 'tar', 'rar'],
    'executables': ['exe', 'msi', 'jar', 'whl'],
    'configuration': ['ini'],
    'torrent': ['torrent']
}

def get_category(extension):
    for category, ext_list in extension_types.items():
        if extension in ext_list:
            return category
    return 'others'

# Change the current working directory to "C:/Users/rahal/Downloads"
os.chdir("C:/Users/rahal/Downloads")

current_directory = os.getcwd()  # Get the updated current directory
print("Current directory:", current_directory)

files = os.listdir(current_directory)

# Store category folder names to avoid moving them later
category_folders = list(extension_types.keys()) + ['others', 'folders']

for file in files:
    full_path = f"{current_directory}/{file}"
    
    # Check if it's a file, not a folder
    if not os.path.isdir(full_path):
        e = file.split(".")
        x = e[-1]  # File extension
        folder = f'{current_directory}/{get_category(x)}'
        
        # Create the folder for the file's category if it doesn't exist
        if not os.path.isdir(folder):
            os.mkdir(folder)
        
        # Check if the file already exists in the destination folder
        destination_file_path = f"{folder}/{file}"
        if not os.path.exists(destination_file_path):
            shutil.move(full_path, destination_file_path)
        else:
            # Rename or skip the file if it already exists
            print(f"File {file} already exists in {folder}. Skipping or renaming...")
    
    # If it's a folder, move it to the 'folders' directory, but exclude category folders
    elif file not in category_folders:
        destination_folder_path = f'{current_directory}/folders/{file}'
        
        # Check if the folder already exists in the destination
        if not os.path.exists(destination_folder_path):
            if not os.path.isdir(f'{current_directory}/folders'):
                os.mkdir(f'{current_directory}/folders')
            
            # Move other folders (not category folders) into 'folders'
            shutil.move(full_path, destination_folder_path)
        else:
            # Handle the case when the destination folder already exists
            print(f"Folder {file} already exists in 'folders'. Skipping or renaming...")
