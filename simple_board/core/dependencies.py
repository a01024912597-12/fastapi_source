from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from utils.security import verify_access_token
from repository.database import get_db
from repository.models.user import User
from exceptions.user import UserNotFoundException, UserCreditialsException
from services.user import get_user


# form submit
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
security = HTTPBearer()

def get_current_user(
    credentials:HTTPAuthorizationCredentials=Depends(security),
    db:Session=Depends(get_db)
):
    
    token = credentials.credentials
    payload = verify_access_token(token)
    user_id = payload.get("sub")

    if user_id is None:
        raise UserCreditialsException

    return get_user(db=db, user_id=user_id)