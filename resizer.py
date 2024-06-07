import os
from PIL import Image

# Function to find all PNG files within the textures subfolders
def find_pngs(base_dir):
    png_files = []
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".png"):
                png_files.append(os.path.join(root, file))
    return png_files

# Function to resize PNG image to 4096x4096 using nearest neighbor method
def resize_image(input_image_path):
    try:
        # Open the image
        image = Image.open(input_image_path)

        # Check if the image is already 4096x4096
        if image.size == (4096, 4096):
            print(f"Image {input_image_path} is already 4096x4096. Skipping.")
            return

        # Resize the image to the desired size using nearest neighbor method
        new_size = (4096, 4096)
        resized_image = image.resize(new_size, Image.NEAREST)

        # Save the resized image, overwriting the original file
        resized_image.save(input_image_path)
        print(f"Resized {input_image_path} successfully.")
    except Exception as e:
        print(f"Error resizing {input_image_path}: {str(e)}")

# Path to the Minecraft resource pack directory
textures_dir = r"" #directory of your resourcepack texture folder

# Find all PNG files within the textures subfolders
png_files = find_pngs(textures_dir)

# Resize each PNG file to 4096x4096 pixels
for png_file in png_files:
    resize_image(png_file)
