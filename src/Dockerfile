FROM python:3.11.4-alpine3.18

WORKDIR /ROOT

# install dep
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -U -r requirements.txt

COPY main.py .

ENTRYPOINT [ "python3", "main.py" ]