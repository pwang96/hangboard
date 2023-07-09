api:
	rm api.yml && \
	python -m service.python.hangboard_service.genspec > api.yml

client:
	npx swagger-typescript-api -p ./api.yml -o ./ui/src/gensrc/api --modular