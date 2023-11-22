import requests
url = "https://raw.githubusercontent.com/Acty101/discord-bot/main/src/face_recognition/data/src/2_people.jpg"
r = requests.get(url)
with open("./temp.jpg", "wb") as f:
  f.write(r.content)