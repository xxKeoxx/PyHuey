from fastapi.responses import JSONResponse
from myfastapi.workflows.hue_connect import setup, discover
from fastapi import APIRouter
from myfastapi.schemas.response_schemas import hue_response

router = APIRouter()

# run setup to get hue IP and setup a user account.
@router.get("/setup", response_model=hue_response)
def setup():
    hub_data = [{"id":"001788fffe227989","internalipaddress":"192.168.4.54","port":443}]
    # hub_data = discover()
    return JSONResponse(content=hub_data)