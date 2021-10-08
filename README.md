# reducto-badge-service

*Only tested locally, not ready for production, the requests definition are 
ill defined to be used from a readme*

Service to generate shields.io badges for reducto reports.

#### Api docs from FastApi

Open [api docs](https://reducto-badge-service.herokuapp.com/docs)

## Run locally

    uvicorn main:app

To test the badge locally:

http://127.0.0.1:8000/badge/reducto_report.json?variable=average_function_length


## From Dockerfile

To deploy from a Docker container:

    sh run.sh


## Deploy to heroku

To deploy the service to Heroku:

- Login to Heroku and fill the info:

    `heroku login`

- Create the app:

    `heroku create reducto-badge-service`

Generates the following 
[app](https://reducto-badge-service.herokuapp.com/).

- Deploy to heroku:

    `git push heroku main`
