import cv2
import os
import glob
from image_processing import func

# Source and Destination
path = "data"
path1 = "data2"

if not os.path.exists(path):
    print(f"Source folder '{path}' not found!")
    exit()

print(f"Mirroring structure from '{path}' to '{path1}'...")

valid_extensions = ('.png', '.jpg', '.jpeg', '.bmp')
all_files = []
for ext in valid_extensions:
    all_files.extend(glob.glob(os.path.join(path, "**", "*" + ext), recursive=True))

if not all_files:
    print(f"No images found in {path}. Check your file extensions!")
    exit()

print(f"📸 Found {len(all_files)} images. Processing...")

var = 0
for img_path in all_files:
    # If path is data/train/A/1.jpg, relative_path becomes train/A/1.jpg
    relative_path = os.path.relpath(img_path, path)

    # Target path becomes data2/train/A/1.jpg
    target_path = os.path.join(path1, relative_path)

    # Create the subfolders (e.g., data2/train/A)
    os.makedirs(os.path.dirname(target_path), exist_ok=True)

    bw_image = func(img_path)

    if bw_image is not None:
        cv2.imwrite(target_path, bw_image)
        var += 1
        if var % 500 == 0:
            print(f"Processed {var} images...")
    else:
        print(f"Skipping unreadable file: {img_path}")

print(f"\nSUCCESS! {var} images processed and saved to '{path1}'.")