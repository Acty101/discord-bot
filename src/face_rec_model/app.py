from PIL import Image, ImageDraw
import face_recognition
import os
from flask import Flask, send_file, request
import requests
import shutil


class FaceRecognitionModel:
    def __init__(self, img_path: str) -> None:
        # Load the jpg file into a numpy array
        self.image = face_recognition.load_image_file(img_path)
        self.face_landmarks_list = face_recognition.face_landmarks(self.image)
        self.img_name = os.path.basename(img_path)

    def apply_lipsticks(self, output_folder: str = "./tmp/") -> str:
        # convert to PIL image
        pil_image = Image.fromarray(self.image)
        for face_landmarks in self.face_landmarks_list:
            draw = ImageDraw.Draw(pil_image, "RGBA")
            draw.polygon(face_landmarks["top_lip"], fill=(150, 0, 0, 128))
            draw.polygon(face_landmarks["bottom_lip"], fill=(150, 0, 0, 128))
            draw.line(face_landmarks["top_lip"], fill=(150, 0, 0, 64), width=8)
            draw.line(face_landmarks["bottom_lip"], fill=(150, 0, 0, 64), width=8)
        if not os.path.exists(output_folder):
            os.mkdir(output_folder)
        file_path = os.path.join(output_folder, f"lipstick_{self.img_name}")
        pil_image.save(file_path)
        print("done")
        return file_path



app = Flask(__name__)
TMP_DIR = "./tmp"

@app.route('/')
def hello():
    return 'Hello, Flask!'

@app.route("/lipstick", methods=["POST"])
def apply_lipstick():
    if request.method != "POST":
        return
    data = request.get_json()
    url = data["url"]
    r = requests.get(url)
    if not os.path.exists(TMP_DIR):
        os.mkdir(TMP_DIR)
    img_path = os.path.join(TMP_DIR, data["filename"])
    with open(img_path, "wb") as f:
        f.write(r.content)
    model = FaceRecognitionModel(img_path=img_path)
    lipstick_img_path = model.apply_lipsticks(TMP_DIR)
    ext = os.path.splitext(os.path.basename(data["filename"]))[1].replace(".", "")
    return send_file(lipstick_img_path)


@app.route("/clean")
def clean():
    """Cleans up tmp dir"""
    shutil.rmtree(TMP_DIR)
    return True


if __name__ == "__main__":
    app.run(debug=True, port=8000)
