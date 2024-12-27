from PIL import Image
import os

# Paths
input_dir = "D:/programming-projects/ml-assignment/additive"  # Folder containing .tif files
output_dir = "D:/programming-projects/ml-assignment/data"  # Folder to save .jpg files
os.makedirs(output_dir, exist_ok=True)

# Crop dimensions for 1024x768 images
# Example: Removing bottom 50 pixels for the scale
crop_box = (0, 0, 1024, 718)  # (left, upper, right, lower)

# Process files sequentially
for i in range(len(os.listdir(input_dir))):  # Adjust the range if files are not contiguous
    file_name = f"micrograph{i}.tif"
    tif_path = os.path.join(input_dir, file_name)
    
    if os.path.exists(tif_path):  # Check if the file exists
        jpg_path = os.path.join(output_dir, f"micrograph{i}.jpg")

        # Open .tif
        with Image.open(tif_path) as img:
            # Crop to remove the scale
            cropped_img = img.crop(crop_box)

            # Resize to 224x224 for ResNet
            resized_img = cropped_img.resize((224, 224))

            # Convert and save as .jpg
            resized_img.convert("RGB").save(jpg_path, "JPEG")
        print(f"Cropped and converted: {file_name} to {jpg_path}")
    else:
        print(f"File not found: {file_name}")

print("All .tif files processed!")
