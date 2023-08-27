from PIL import Image
from torch import Tensor
import os

def crop_img(src: str, dest: str, coords: list) -> None:
    """Crops the img at <src> into <dest> based on all the coordinates found in <coords>"""
    img = Image.open(src)
    for i, coord in enumerate(coords):
        # Crop the image
        cropped_img = img.crop(coord)
        # Save the cropped image
        cropped_img.save(os.path.join(dest, str(i)))

def process_coords(coords):
    if isinstance(coords, Tensor):
        coords = coords.tolist()
    return coords