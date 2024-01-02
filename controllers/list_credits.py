from fastapi import HTTPException, status

from db.db import data

def list_credits():

    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No credit available")
    
    return data