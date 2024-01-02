from fastapi import HTTPException, status

# Importing the data variable from the db module
from db.db import data

def get_credit(id: str):
    """Get credit API controller"""
    
    # Iterate through each item in the global data list
    for item in data:
        # Check if the "id" of the current item matches the specified ID
        if item["id"] == id:
            # Return the credit data if a match is found
            return item
    
    # Raise an HTTPException with a 404 Not Found status code and a detail message
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No credit found with id: {id}")
