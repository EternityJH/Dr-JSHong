import fitz
import sys
from PIL import Image

doc = fitz.open("assets/CV_洪佳聖_AItewan.pdf")
page = doc[0]
pix = page.get_pixmap(dpi=36)
pix.save("page0.png")

def image_to_ascii(image_path, new_width=60):
    img = Image.open(image_path).convert('L')
    width, height = img.size
    aspect_ratio = height / float(width)
    new_height = int(aspect_ratio * new_width * 0.5)
    img = img.resize((new_width, new_height))
    
    pixels = img.getdata()
    chars = ["@", "J", "D", "%", "*", "P", "+", "Y", "$", ",", "."]
    
    new_pixels = [chars[pixel//25] for pixel in pixels]
    new_pixels = ''.join(new_pixels)
    
    ascii_image = [new_pixels[index:index + new_width] for index in range(0, len(new_pixels), new_width)]
    print(f"--- ASCII Art of {image_path} ---")
    print("\n".join(ascii_image))

image_to_ascii("page0.png")
