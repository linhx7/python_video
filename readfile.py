import os
import glob

# Specify the relative folder path
folder_path = '.\\in'

# Use glob to find all files in the folder
files = glob.glob(os.path.join(folder_path, '*'))

# Loop through and read each file
for file_path in files:
    filename = os.path.basename(file_path)
    print(filename)
