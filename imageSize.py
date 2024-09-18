from PIL import Image

def find_image_resolution(image_path):
    with Image.open(image_path) as img:
        width, height = img.size
    return width, height


image_path = 'use image path of your system'
width, height = find_image_resolution(image_path)
print(f"The resolution of the image is {width}x{height}")
