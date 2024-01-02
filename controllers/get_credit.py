from fastapi import HTTPException, status

from db.db import data

def get_credit(id: str):

    for item in data:
        if item["id"] == id:
            return item
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No credit found with id: {id}")

