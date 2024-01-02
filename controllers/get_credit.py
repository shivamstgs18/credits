from fastapi import HTTPException, status

# Importing the data variable from the db module
from db.db import data

def get_credit(user_id: str):
    """Get credit API controller"""
    if not user_id in data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid user_id")
    
    credit_data = data[user_id]
    
    # Raise an HTTPException with a 404 Not Found status code and a detail message
    if not credit_data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No credit found for user_id: {user_id}")
    
    return credit_data
