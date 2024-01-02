from fastapi import HTTPException, status

# Importing the data variable from the db module and the UpdateCreditparam parameter class
from db.db import data
from params import UpdateCreditparam

def get_index(id: str):
    """Get Index of Credit API controller"""
    
    # Iterate through each index and item in the global data list
    for ind, item in enumerate(data):
        # Check if the "id" of the current item matches the specified ID
        if item["id"] == id:
            # Return the index if a match is found
            return ind
    
    # Raise an HTTPException with a 404 Not Found status code and a detail message
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No data found to update for credit_id: {id}")

def put_credit(credit_data: UpdateCreditparam):
    """Update Credit API controller"""
    
    # Access the global data variable, which is a list storing credit records
    global data

    # Get the index of the credit record to be updated using the get_index function
    data_ind = get_index(credit_data.id)
    
    # Iterate through key-value pairs in the UpdateCreditparam object
    for key, value in credit_data.__dict__.items():
        # Check if the value is not None, and update the corresponding key in the global data list
        if value is not None:
            data[data_ind][key] = value

    # Return a success response
    return {"Success": True}
