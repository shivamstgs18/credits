# Importing the get_credit function from the get_credit module
from controllers.get_credit import get_credit

# Importing the data variable from the db module
from db.db import data

def delete_credit(id: str):
    """Delete credit API controller"""
    
    # Access the global data variable, which is a list storing credit records
    global data

    # Retrieve the credit data associated with the given ID using the get_credit function
    credit_data = get_credit(id)

    # Remove the retrieved credit data from the global data list
    data.remove(credit_data)

    # Return a success response
    return {"Success": True}
