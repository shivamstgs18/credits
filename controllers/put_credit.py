from fastapi import HTTPException, status

from db.db import data
from params import UpdateCreditparam

def get_index(id: str):

    for ind, item in enumerate(data):
        if(item["id"] == id):
            return ind
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No data found to update for credit_id: {id}")

def put_credit(credit_data: UpdateCreditparam):
    global data

    data_ind = get_index(credit_data.id)
    
    for key, value in (credit_data.__dict__).items():

        if value is not None:
            data[data_ind][key] = value

    return {"Success": True}