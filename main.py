r"""FastAPI app service.

Functionalities to implement:
- Endpoint to read a report from current workind directory
    Expect a .reducto_report.json in the folder root
- Parse the file to obtain the data
- Generate request for shields.io (personalized by one of the variables initially):
    i.e. https://img.shields.io/badge/python-hey-green
- Obtain the image returned by the server
- Serve the image
"""

import io

from fastapi import FastAPI, File, UploadFile
from starlette.responses import StreamingResponse

app = FastAPI()


@app.get("/report/{file_path:path}")
async def read_file(file_path: str):
    """Function to read a file (expected to be at the same level of this very file.

    TODO:
        Create a sample file for testing purposes.

    Parameters
    ----------
    file_path : str
        Name of the file. As expected in relative, should be the only info necessary.
    """
    with open(file_path, 'r') as f:
        data = f.read()
    return {"file_path": data}
