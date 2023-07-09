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
npx swagger-typescript-api -p ./api.yml -o ./ui/src/gensrc/api --modular
```