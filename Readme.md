# 3megawatt Solar Power Plant - Back-end 

Collects data from monitoring services and also generate suitable reports for visualization of the data of various solar power plants.

## Usage Instructions

1. To spin up the Docker with production settings, use this single command. 
`` docker-compose up --build ``

2. Open your browser and visit `localhost:8000/api/v1/plants/` or `127.0.0.1:8000/api/v1/plants/` to access the API

[API Documentation](docs/api.md)

To run test cases:
1. `docker-compose exec web python manage.py test`


