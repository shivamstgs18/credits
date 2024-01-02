from fastapi import HTTPException, status

from db.db import users

def get_user_by_username(username: str):

    for item in users:

        if item['username'] == username:
            return item
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No user available for username: {username}")