api:
	rm api.yml && \
	python -m service.python.hangboard_service.genspec > api.yml
