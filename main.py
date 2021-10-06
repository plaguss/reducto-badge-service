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

from typing import Dict, Optional
import json
from enum import Enum

from jsonschema import validate, ValidationError
import aiofiles
from fastapi import FastAPI
from fastapi.responses import RedirectResponse


BASE_URL = r'https://img.shields.io/badge/<LABEL>-<MESSAGE>-green?logo=python&color=ffd43b'
# Variables to be replaced
LABEL = '<LABEL>'
MESSAGE = '<MESSAGE>'


class ReductoVariables(str, Enum):
    """Variables allowed to be returned from the report. """
    average_function_length = "average_function_length"
    blank_lines = "blank_lines"
    comment_lines = "comment_lines"
    docstring_lines = "docstring_lines"
    lines = "lines"
    number_of_functions = "number_of_functions"
    source_files = "source_files"
    source_lines = "source_lines"


schema = {
    "type": "object",
    "minProperties": 1,
    "maxProperties": 1,
    "properties": {
        "package_name": {
            "type": "object",
            "minProperties": 7,
            "maxProperties": 8,
            "properties": {
                "average_function_length": {"type": "number"},
                "blank_lines": {"type": ["number", "string"]},
                "comment_lines": {"type": ["number", "string"]},
                "docstring_lines": {"type": ["number", "string"]},
                "source_lines": {"type": ["number", "string"]},
                "lines": {"type": "number"},
                "number_of_functions": {"type": "number"},
                "source_files": {"type": "number"}
            },
            "required": [
                "average_function_length", "blank_lines", "comment_lines",
                "docstring_lines", "source_lines", "lines", "number_of_functions"
            ]
        }
    }
}


app = FastAPI()


async def read_report(file_path: str) -> Dict:
    """Read a json file asynchronously.

    Parameters
    ----------
    file_path : str
        Path to the file

    Returns
    -------
    data : file
        Returns the parsed json as a dict
    """
    async with aiofiles.open(file_path, mode='r') as f:
        data = await f.readlines()
        report = json.loads(''.join(data))

        try:
            validate(report, schema)  # If incorrect schema, returns ValidationError
        except ValidationError as exc:
            print(f"Validation failed on report: {report}.")
            print("Check expected format: https://reducto.readthedocs.io/en/latest/")
            raise exc

        # If the validation passed, extract inner report:
        package_name: str = list(report.keys())[0]
        return report[package_name]


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
    return await read_report(file_path)


def generate_url(variable: str, report: Dict) -> str:
    """Generates the url to be requested to shields.io.

    Parameters
    ----------
    variable : str
        Variable from reducto_report.json.
    report : dict
        Report from json, with package name already filtered.

    Returns
    -------
    url : str
        URL to be requested.
    """
    return BASE_URL.replace(LABEL, variable).replace(MESSAGE, str(report[variable]))


@app.get("/badge/{file_path:path}", response_class=RedirectResponse)
async def get_badge(file_path: str, variable: Optional[ReductoVariables] = None):
    """Obtain the badge from the server.

    Parameters
    ----------
    file_path : str
        Path (expected relative) to the reducto_report.json file.
    variable : ReductoVariables

    Examples
    --------
    Default url:
    http://127.0.0.1:8000/badge/reducto_report.json

    Requesting one of the variables:
    http://127.0.0.1:8000/badge/reducto_report.json?variable=lines
    http://127.0.0.1:8000/badge/reducto_report.json?variable=average_function_length
    """
    report: Dict = await read_report(file_path)
    if variable is None:
        variable = ReductoVariables.lines

    return generate_url(variable, report)
