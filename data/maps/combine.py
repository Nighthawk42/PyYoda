import os
from tqdm import tqdm

# Set the directory path where your folders are located
directory_path = r"C:\Users\Nighthawk\Desktop\PyYoda\data\maps"

# Get a list of all folders in the directory
folders = [folder for folder in os.listdir(directory_path) if os.path.isdir(os.path.join(directory_path, folder))]

# Create a progress bar
progress_bar = tqdm(folders, desc="Renaming files")

# Iterate through each folder
for folder in progress_bar:
    folder_path = os.path.join(directory_path, folder)
    combined_file_path = os.path.join(folder_path, "combined.png")
    new_file_name = os.path.join(folder_path, folder + ".jpg")

    # Check if the combined.png file exists in the folder
    if os.path.exists(combined_file_path):
        # Rename the combined.png file to <folder_name>.jpg
        os.rename(combined_file_path, new_file_name)
        progress_bar.set_postfix({"Renamed": folder})
    else:
        progress_bar.set_postfix({"File not found": folder})

# Close the progress bar
progress_bar.close()