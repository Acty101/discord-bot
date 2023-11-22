build:
	docker build -t discord . 
run:
	docker run --gpus all  --env-file .env discord
compose:
	docker compose up --build --remove-orphans