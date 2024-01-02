from fastapi import HTTPException, status

from db.db import data

def get_index(user_id: str, id: str):
    """Get Index of Credit API controller"""
    
    # Iterate through each index and item in the global data list
    for ind, item in enumerate(data[user_id]):
        # Check if the "id" of the current item matches the specified ID
        if item["id"] == id:
            # Return the index if a match is found
            return ind
    
    # Raise an HTTPException with a 404 Not Found status code and a detail message
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No data found to update for credit_id: {id} and user_id: {user_id}")