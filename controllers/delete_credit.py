# Importing the get_credit function from the get_credit module
from helpers import get_index


# Importing the data variable from the db module
from db.db import data

def delete_credit(user_id: str, id: str):
    """Delete credit API controller"""
    
    # Access the global data variable, which is a list storing credit records
    global data

    # Retrieve the credit data associated with the given ID using the get_credit function
    data_ind = get_index(user_id, id)

    # Remove the retrieved credit data from the global data list
    del data[user_id][data_ind]

    # Return a success response
    return {"Success": True}
