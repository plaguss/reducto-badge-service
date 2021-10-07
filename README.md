# reducto-badge-service
Service to generate shields.io badges for reducto reports

![badge](http://127.0.0.1:8000/sample_badge)

#![test](http://0.0.0.0:8080/badge/reducto_report.json)

#![test2](http://0.0.0.0:8080/badge/home/agustin/github_repos/reducto-badge-service/reducto_report.json)

#![test1](http://127.0.0.1:8000/badge/reducto_report.json)

#![test1](http://127.0.0.1:8000/badge/reducto_report.json?variable=average_function_length)

## Run locally

    uvicorn main:app

#### From Dockerfile

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
    
    `heroku open`

