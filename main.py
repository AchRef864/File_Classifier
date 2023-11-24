import os
import glob

# Change the current working directory to "C:/Users/rahal/Downloads"
os.chdir("C:/Users/rahal/Downloads")

current_directory = os.getcwd()  # Get the updated current directory
print("Current directory:", current_directory)

pdf_files = glob.glob(os.path.join(current_directory, "*.pdf"))
number_of_pdf_files = len(pdf_files)
print("Number of PDF files in the current directory:", number_of_pdf_files)

jpeg_files = glob.glob(os.path.join(current_directory, "*.jpeg"))
number_of_jpeg_files = len(jpeg_files)
print("Number of jpeg files in the current directory:", number_of_jpeg_files)

jpg_files = glob.glob(os.path.join(current_directory, "*.jpg"))
number_of_jpg_files = len(jpg_files)
print("Number of jpg files in the current directory:", number_of_jpg_files)

png_files = glob.glob(os.path.join(current_directory, "*.png"))
number_of_png_files = len(jpg_files)
print("Number of png files in the current directory:", number_of_png_files)

folders = [f for f in os.listdir(current_directory) if os.path.isdir(f)]
number_of_folders = len(folders)
print("Number of folders in the current directory:", number_of_folders)
