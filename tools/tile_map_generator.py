import os
import json
from PIL import Image
from tqdm import tqdm  # for progress bar

# Define input and output directories
input_dir = "../data/tiles"
output_dir = "../data/tiles"

# Define tile size and number of tiles
tile_size = 32
num_tiles = 2123

# Define metadata keys
metadata_keys = ["ID", "Filename", "Type", "Name", "Description", "X", "Y"]

# Create empty list to store tile metadata
tile_metadata = []

# Compute number of rows and columns in tile map
num_cols = int(num_tiles ** 0.5)
num_rows = (num_tiles + num_cols - 1) // num_cols  # round up division

# Create empty image to store tile map
tile_map = Image.new("RGBA", (tile_size * num_cols, tile_size * num_rows), (0, 0, 0, 0))

# Loop through all tiles and create metadata and tile map
for i in tqdm(range(num_tiles)):
    # Define filename and ID
    filename = f"{i}.png"
    tile_id = i

    # Define type, name, and description
    tile_type = "Terrain"  # Change this as necessary
    tile_name = f"Tile {i}"  # Change this as necessary
    tile_description = f"This is tile {i}"  # Change this as necessary

    # Define X and Y position in tile map array
    tile_x = i % num_cols
    tile_y = i // num_cols

    # Add metadata to list
    tile_metadata.append(dict(zip(metadata_keys, [tile_id, filename, tile_type, tile_name, tile_description, tile_x, tile_y])))

    # Load tile image and paste into tile map
    tile_path = os.path.join(input_dir, filename)
    try:
        with Image.open(tile_path) as tile_image:
            tile_map.paste(tile_image, (tile_x * tile_size, tile_y * tile_size))
    except FileNotFoundError as e:
        print(f"Error: {e}")
        continue

# Save tile map to output directory
tile_map_path = os.path.join(output_dir, "tile_map.png")
tile_map.save(tile_map_path)

# Write metadata to JSON file
metadata_file = os.path.join(output_dir, "tile_metadata.json")
with open(metadata_file, "w") as f:
    json.dump(tile_metadata, f, indent=4)

print("Tile Map Generated!")