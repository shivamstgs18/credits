from uuid import uuid4
from fastapi import HTTPException, status
from params import PostCreditParam

# Importing the data variable from the db module
from db.db import data

def add_credit(user_id: str, credit_data: PostCreditParam):
    """Add credit API controller"""
    
    # Access the global data variable, which is a list storing credit records
    global data

    # Generate a new UUID for the credit record
    credit = {
        "id": uuid4()
    }

    # Update the credit dictionary with the values from the incoming PostCreditParam
    credit.update(credit_data.__dict__)

    # Append the new credit record to the data list
    data[user_id].append(credit)
    
    # Return a success response with the generated credit ID
    return {"Success": True, "id": credit["id"]}
