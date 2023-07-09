# hangboard


# Service
## Running the app in development
```
cd service/python/hangboard_service
flask run
```

# UI
## Generating api.yml
There is now a Makefile, so the easiest is to use `make api`.

Alternatively, this is the way to do it:
```
rm api.yml
python -m service.python.hangboard_service.genspec > api.yml
```
## Generating the Typescript
The easiest way to use this is `make client`.

Alternatively, you can run the following command:
```
npx swagger-typescript-api -p ./api.yml -o ./ui/src/gensrc/api --modular
```