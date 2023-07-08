# hangboard


# Service
## Running the app in development
```
cd service/python/hangboard_service
flask run
```

# UI
## Generating api.yml
```
rm api.yml
python -m service.python.hangboard_service.genspec > api.yml
```
## Generating the Typescript
With the service running:
```
npx swagger-typescript-api -p http://127.0.0.1:5000/api/swagger.json -o ./src/gensrc/api --modular
```