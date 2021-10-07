# reducto-badge-service
Service to generate shields.io badges for reducto reports

Sample badges, by passing the reducto report at the root of the package, and passing the 
name of the variable wanted:

---

![badge](https://reducto-badge-service.herokuapp.com/badge/reducto_report.json)

![badge](https://reducto-badge-service.herokuapp.com/badge/reducto_report.json?variable=source_lines)

![badge](https://reducto-badge-service.herokuapp.com/badge/reducto_report.json?variable=blank_lines)

![badge](https://reducto-badge-service.herokuapp.com/badge/reducto_report.json?variable=comment_lines)

![badge](https://reducto-badge-service.herokuapp.com/badge/reducto_report.json?variable=docstring_lines)

![badge](https://reducto-badge-service.herokuapp.com/badge/reducto_report.json?variable=average_function_length)

![badge](https://reducto-badge-service.herokuapp.com/badge/reducto_report.json?variable=number_of_functions)

![badge](https://reducto-badge-service.herokuapp.com/badge/reducto_report.json?variable=source_files)
---

#### Api docs from FastApi

Open [api docs](https://reducto-badge-service.herokuapp.com/docs)

## Run locally

    uvicorn main:app

To test the badge locally:
#![test](http://127.0.0.1:8000/badge/reducto_report.json?variable=average_function_length)


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
