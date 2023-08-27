import utils
import os
import shutil


from groundingdino.util.inference import (
    load_model,
    load_image,
    predict,
)

model = load_model(
    "GroundingDINO/groundingdino/config/GroundingDINO_SwinT_OGC.py",
    "weights/groundingdino_swint_ogc.pth",
)

# paths to image source and destination
src = os.path.join(os.getcwd(),"data/src")
dest = os.path.join(os.getcwd(),"data/dest")
BOX_TRESHOLD = 0.35
TEXT_TRESHOLD = 0.25


def load_and_predict(image_path, text_prompt: str):
    _, image = load_image(image_path)

    boxes, logits, phrases = predict(
        model=model,
        image=image,
        caption=text_prompt,
        box_threshold=BOX_TRESHOLD,
        text_threshold=TEXT_TRESHOLD,
    )
    return boxes, logits, phrases


def main():
    """Looks through all images in <src> for faces and crops each face to <dest>"""
    img_names = os.listdir(src)
    for name in img_names:
        path = os.path.join(src, name)
        # only need boxes of coords to crop
        boxes, _, _ = load_and_predict(path, "person")

        # create a folder name for each img since many images generated from one
        current_folder = os.path.join(dest, name)

        # start from clean folder each time
        if os.path.exists(current_folder):
            shutil.rmtree(current_folder)
        os.makedirs(current_folder)
        coords = utils.process_coords(boxes)

        # crop and save images
        utils.crop_img(src=path, dest=current_folder, coords=coords)


if __name__ == "__main__":
    main()