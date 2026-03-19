import sys
from PIL import Image

for file in ["cv_extracted_image_0.png", "assets/images/headshot.jpg"]:
    try:
        img = Image.open(file)
        print(f"{file}: {img.format} {img.size} {img.mode}")
    except Exception as e:
        print(f"Error opening {file}: {e}")
