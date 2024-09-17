import os
import glob
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

extensions = []
folders = []

for file in files :
    if(not os.path.isdir(f"{current_directory}/{file}")):
        e = file.split(".")
        x = e[len(e)-1]
        folder = f'{current_directory}/{get_category(x)}'
        if(not os.path.isdir(folder)):
            os.mkdir(folder)
            shutil.move(f"{current_directory}/{file}",f"{current_directory}/{get_category(x)}/{file}")
        else :
            shutil.move(f"{current_directory}/{file}",f"{current_directory}/{get_category(x)}/{file}")
        
    else:
        if(not os.path.isdir(f'{current_directory}/folders')):
            os.mkdir(f'{current_directory}/folders')
            shutil.move(f"{current_directory}/{file}",f"{current_directory}/folders/{file}")
        else :
            shutil.move(f"{current_directory}/{file}",f"{current_directory}/folders/{file}")
        folders.append(file)

