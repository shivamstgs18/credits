from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

# Importing custom parameter classes
from params import PostCreditParam, UpdateCreditparam

# Importing controller functions
from controllers.list_credits import list_credits
from controllers.get_credit import get_credit
from controllers.add_credit import add_credit
from controllers.put_credit import put_credit
from controllers.delete_credit import delete_credit

# Creating a FastAPI instance
app = FastAPI()

# API endpoint to list all credit data
@app.get('/credits')
def list_credits_api():
    """API to list all credit data"""

    # Call controller function to get credit list
    resp = jsonable_encoder(list_credits())

    # Return JSON response with a 200 OK status code
    return JSONResponse(status_code=status.HTTP_200_OK, content=resp)

# API endpoint to get credit by ID
@app.get('/credits/')
def get_credit_api(id: str):
    # Call controller function to get credit by ID
    resp = jsonable_encoder(get_credit(id))

    # Return JSON response with a 200 OK status code
    return JSONResponse(status_code=status.HTTP_200_OK, content=resp)

# API endpoint to add a new credit record
@app.post('/credits')
def add_credit_api(request: PostCreditParam):
    # Call controller function to add a new credit record
    resp = jsonable_encoder(add_credit(request))

    # Return JSON response with a 201 Created status code
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=resp)

# API endpoint to update an existing credit record
@app.put('/credits/')
def put_credit_api(request: UpdateCreditparam):
    # Call controller function to update an existing credit record
    resp = jsonable_encoder(put_credit(request))

    # Return JSON response with a 200 OK status code
    return JSONResponse(status_code=status.HTTP_200_OK, content=resp)

# API endpoint to delete a credit record by ID
@app.delete('/credit/')
def delete_credit_api(id: str):
    # Call controller function to delete a credit record by ID
    resp = jsonable_encoder(delete_credit(id))

    # Return JSON response with a 200 OK status code
    return JSONResponse(status_code=status.HTTP_200_OK, content=resp)
