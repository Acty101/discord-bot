FROM python:3.11.4-alpine3.18

WORKDIR /ROOT

# install dep
RUN python3 -m pip install -U discord.py python-dotenv

COPY main.py .

ENTRYPOINT [ "python3", "main.py" ]