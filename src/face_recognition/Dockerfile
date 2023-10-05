FROM animcogn/face_recognition:gpu

WORKDIR /ROOT

# COPY requirements.txt requirements.txt

# RUN pip3 install -r ./requirements.txt

COPY main.py ./
COPY data data
RUN mkdir output

CMD [ "python3", "main.py" ]