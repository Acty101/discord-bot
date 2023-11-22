import requests
from io import BytesIO
from PIL import Image


url = "https://raw.githubusercontent.com/Acty101/discord-bot/main/src/face_recognition/data/src/2_people.jpg"
filename = "face.jpg"
data = {"url": url, "filename": filename}
response = requests.post(f'http://localhost:8000/lipstick', json=data)
if response.status_code == 200:
    image_data = response.content
    with open('downloaded_image.jpg', 'wb') as file:
        file.write(image_data)
    img = Image.open('./downloaded_image.jpg')
    if img:
        img.show()
    else:
        print("Image is None.")
    
else:
    print(f"Error displaying image")