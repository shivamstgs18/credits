from fastapi import APIRouter, HTTPException, status
from fastapi.param_functions import Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from controllers.get_user import get_user_by_username

from auth.oauth2 import create_access_token
router = APIRouter(
    tags=['authentication']
)

@router.post('/token')
def get_token(request: OAuth2PasswordRequestForm = Depends()):
    user = get_user_by_username(request.username)

    if not user:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail="User not found with this username")
    
    access_token = create_access_token(data={'sub' : user["username"]})

    return {
        'access_token':  access_token,
        'token_type': 'bearer',
        'user_id': user["id"],
        'username': user["username"]
    }
