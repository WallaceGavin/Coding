#!/usr/bin/env python3

import os
from shutil import move

# Path to your Downloads folder
downloads_path = os.path.expanduser('~/Downloads')
pdf_folder = os.path.join(downloads_path, 'PDFs')
image_folder = os.path.join(downloads_path, 'Images')

# Create folders if they don't exist
os.makedirs(pdf_folder, exist_ok=True)
os.makedirs(image_folder, exist_ok=True)

# File extensions for images
image_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.dng']

# Scan all files and move them to respective folders
for file in os.listdir(downloads_path):
	full_file_path = os.path.join(downloads_path, file)
	if os.path.isfile(full_file_path):
		filename, file_extension = os.path.splitext(file)
		if file_extension.lower() == '.pdf':
			move(full_file_path, os.path.join(pdf_folder, file))
		elif file_extension.lower() in image_extensions:
			move(full_file_path, os.path.join(image_folder, file))
			
print("Files have been organized!")
