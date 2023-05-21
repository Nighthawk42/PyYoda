# GIF 2 Frames - A tool to convert a GIF file to a series of PNG frames.

import os
from PIL import Image
from tkinter import filedialog, Tk
from tqdm import tqdm

# Create a Tkinter root window
root = Tk()
root.withdraw()  # Hide the root window

# Open a file dialog to select a GIF file
gif_path = filedialog.askopenfilename(filetypes=[("GIF Files", "*.gif")])

if gif_path:
    try:
        # Open the selected GIF file
        gif = Image.open(gif_path)

        # Extract the directory path and file name (excluding extension)
        directory_path, file_name = os.path.split(gif_path)
        file_name = os.path.splitext(file_name)[0]

        # Create a directory to save the PNG frames
        output_dir = os.path.join(directory_path, file_name)
        os.makedirs(output_dir, exist_ok=True)

        # Initialize the progress bar
        progress_bar = tqdm(total=gif.n_frames, unit="frame")

        # Iterate through each frame in the GIF and save it as a PNG
        for frame in range(gif.n_frames):
            # Select the current frame
            gif.seek(frame)

            # Convert the frame to RGBA format (if necessary) and save as PNG
            frame_img = gif.convert("RGBA")
            frame_filename = os.path.join(output_dir, f"frame_{frame}.png")
            frame_img.save(frame_filename, format="png")

            # Update the progress bar
            progress_bar.update(1)

        # Complete message
        print("Conversion completed successfully!")

    except Exception as e:
        # Error statement
        print(f"An error occurred: {str(e)}")
else:
    # User canceled the file selection
    print("File selection canceled by the user.")
