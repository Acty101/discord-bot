FROM animcogn/face_recognition:gpu

WORKDIR /ROOT

COPY requirements.txt requirements.txt

RUN pip3 install --upgrade pip && pip install -r requirements.txt

COPY app.py .
COPY data data
RUN mkdir tmp

EXPOSE 8000

ENTRYPOINT [ "flask", "run", "--host", "0.0.0.0", "--port", "8000"]