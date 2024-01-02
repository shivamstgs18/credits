from fastapi import HTTPException, status

# Importing the data variable from the db module
from db.db import data

def list_credits():
    """List Credits API controller"""
    
    # Check if the global data list is empty
    if not data:
        # Raise an HTTPException with a 404 Not Found status code and a detail message
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No credit available")
    
    # Return the global data list if it is not empty
    return data
