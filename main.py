from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from params import PostCreditParam, UpdateCreditparam

from controllers.list_credits import list_credits
from controllers.get_credit import get_credit
from controllers.add_credit import add_credit
from controllers.put_credit import put_credit
from controllers.delete_credit import delete_credit

app = FastAPI()

@app.get('/credits')
def list_credits_api():
    """API to list all credit data"""

    resp = jsonable_encoder(list_credits())
    return JSONResponse(status_code=status.HTTP_200_OK, content=resp)

@app.get('/credits/')
def get_credit_api(id: str):
    resp = jsonable_encoder(get_credit(id))
    return JSONResponse(status_code=status.HTTP_200_OK, content=resp)

@app.post('/credits')
def add_credit_api(request: PostCreditParam):
    resp = jsonable_encoder(add_credit(request))
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=resp)

@app.put('/credits/')
def put_credit_api(request: UpdateCreditparam):
    resp = jsonable_encoder(put_credit(request))
    return JSONResponse(status_code=status.HTTP_200_OK, content=resp)

@app.delete('/credit/')
def delete_credit_api(id: str):
    resp = jsonable_encoder(delete_credit(id))
    return JSONResponse(status_code=status.HTTP_200_OK, content=resp)
