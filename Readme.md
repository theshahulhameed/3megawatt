# 3megawatt Solar Power Plant - Back-end 
Manages the back-end infrastructure of a solar power plant service. 

**Functionalities**
- Collects data from monitoring service and updates the data points periodically as well as programatically on custom request. 
- Generate suitable reports for visualization of the data of various solar power plants.

**Technologies used**
`` Python, Django, PostgreSQL, Redis, Celery, Docker ``

## Usage Instructions

1. To spin up the Docker with production settings, use this single command. 
`` docker-compose up --build ``

2. Open your browser and visit `localhost:1337/api/v1/plants/` or `127.0.0.1:1337/api/v1/plants/` to access the API

[API Documentation](docs/api.md)

To run test cases:
1. `docker-compose exec web python manage.py test`


