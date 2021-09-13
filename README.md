# Risk Module Backend

## Backend Server Setup
```
# Build docker image
docker-compose build

# Start container
docker-compose up
```

## Run Migrations
`docker-compose exec server bash -c python manage.py migrate`
