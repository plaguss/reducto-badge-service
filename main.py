r"""FastAPI app service.

Functionalities to implement:
- Endpoint to read a report from current workind directory
    Expect a .reducto_report.json in the folder root
- Parse the file to obtain the data
- Generate request for shields.io (personalized by one of the variables initially):
    i.e. https://img.shields.io/badge/python-hey-green
- Obtain the image returned by the server
- Serve the image

TODO:
    - Idea to serve the images:
    https://stackoverflow.com/questions/55873174/how-do-i-return-an-image-in-fastapi/67497103#67497103

TODO:
    RedirectResponse
    - Parse file
    - Generate url

    - To obtain a varaible from json file.
    https://fastapi.tiangolo.com/tutorial/query-params/


Python colors:
https://www.schemecolor.com/python-logo-colors.php


"""

from enum import Enum
import json

from fastapi import FastAPI
from fastapi.responses import RedirectResponse

BASE_URL = r'https://img.shields.io/badge/<LABEL>-<MESSAGE>-<COLOR>?logo=python'

app = FastAPI()


class ReductoVariables(str, Enum):
    average_function_length = 'average_function_length'


@app.get("/report/{file_path:path}")
async def read_file(file_path: str):
    """Function to read a file (expected to be at the same level of this very file.

    TODO:
        Create a sample file for testing purposes.

    Parameters
    ----------
    file_path : str
        Name of the file. As expected in relative, should be the only info necessary.

    Examples
    --------
    http://127.0.0.1:8000/report/reducto_report.json
    """
    with open(file_path, 'r') as f:
        data = json.load(f)
    return {"file_path": data}


@app.get("/sample_badge", response_class=RedirectResponse)
async def badge():
    """Function to read a file (expected to be at the same level of this very file.

    TODO:
        Create a sample file for testing purposes.

    Parameters
    ----------
    file_path : str
        Name of the file. As expected in relative, should be the only info necessary.

    Examples
    --------
    http://127.0.0.1:8000/report
    """
    return r'https://shields.io/badge/python-hey-green'
    # return get_badge()
    # return Response(content=get_badge(), media_type="image/svg")
