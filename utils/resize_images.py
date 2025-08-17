# import os
# from PIL import Image

# def resize_images_to_square(root_dir):
#     for subdir, dirs, files in os.walk(root_dir):
#         for file in files:
#             if file.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.tiff')):
#                 full_path = os.path.join(subdir, file)
#                 try:
#                     with Image.open(full_path) as img:
#                         # Define the size for the square image (use the smallest dimension to avoid upscaling)
#                         min_side = min(img.size)
                        
#                         # Calculate the cropping box centered
#                         left = (img.width - min_side) // 2
#                         top = (img.height - min_side) // 2
#                         right = left + min_side
#                         bottom = top + min_side
                        
#                         img_cropped = img.crop((left, top, right, bottom))

#                         # Save the image replacing the original in the same path
#                         img_cropped.save(full_path)
#                         print(f"Processed {full_path}")
#                 except Exception as e:
#                     print(f"Error processing {full_path}: {e}")

# # Change 'data' to your root directory where images are
# resize_images_to_square('data')
import os
from PIL import Image

def resize_images_to_640x640(root_dir):
    target_size = (640, 640)
    for subdir, dirs, files in os.walk(root_dir):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.tiff')):
                full_path = os.path.join(subdir, file)
                try:
                    with Image.open(full_path) as img:
                        # Resize image to 640x640 while keeping aspect ratio by cropping to square first
                        min_side = min(img.size)
                        left = (img.width - min_side) // 2
                        top = (img.height - min_side) // 2
                        right = left + min_side
                        bottom = top + min_side
                        img_cropped = img.crop((left, top, right, bottom))
                        
                        img_resized = img_cropped.resize(target_size, Image.Resampling.LANCZOS)

                        # Save image replacing the original in the same path
                        img_resized.save(full_path)
                        print(f"Resized {full_path} to 640x640")
                except Exception as e:
                    print(f"Error processing {full_path}: {e}")

# Change 'data' to your root directory where images are
resize_images_to_640x640('data')
