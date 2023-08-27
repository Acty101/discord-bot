FROM nvidia/cuda:11.7.1-devel-ubuntu20.04 as release

WORKDIR /root

# Install python deps
RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt-get -y install tzdata && \
    apt-get install --no-install-recommends -y build-essential software-properties-common && \
    add-apt-repository -y ppa:deadsnakes/ppa && \
    apt-get update && \
    apt-get install -y python3.8 python3-pip python3-distutils python3-venv gcc ffmpeg libsm6 libxext6 git wget && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# install grounding DINO deps
ENV CUDA_HOME "/usr/local/cuda-11.7"
RUN git clone https://github.com/IDEA-Research/GroundingDINO.git
RUN cd GroundingDINO && pip install --upgrade pip && pip install -r requirements.txt && pip install .

# donwload GD weights
RUN mkdir weights && cd weights \
    && wget -q https://github.com/IDEA-Research/GroundingDINO/releases/download/v0.1.0-alpha/groundingdino_swint_ogc.pth

COPY main.py utils.py ./
COPY data ./data

CMD ["python3", "main.py"]