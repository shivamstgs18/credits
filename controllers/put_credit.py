from fastapi import HTTPException, status

# Importing the data variable from the db module and the UpdateCreditparam parameter class
from db.db import data
from params import UpdateCreditparam
from helpers import get_index

def put_credit(user_id: str, credit_data: UpdateCreditparam):
    """Update Credit API controller"""
    
    # Access the global data variable, which is a list storing credit records
    global data

    # Get the index of the credit record to be updated using the get_index function
    data_ind = get_index(user_id, credit_data.id)
    
    # Iterate through key-value pairs in the UpdateCreditparam object
    for key, value in credit_data.__dict__.items():
        # Check if the value is not None, and update the corresponding key in the global data list
        if value is not None:
            data[user_id][data_ind][key] = value

    # Return a success response
    return {"Success": True}
