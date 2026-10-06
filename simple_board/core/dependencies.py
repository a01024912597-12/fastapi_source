from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from utils.security import verify_access_token
from repository.database import get_db
from repository.models.user import User
from exceptions.user import UserNotFoundException, UserCreditialsException

# form submit
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
security = HTTPBearer()

def get_current_user(credentials:HTTPAuthorizationCredentials=Depends(security), db:Session=Depends(get_db)):
    token = credentials.credentials
    payload = verify_access_token(token)
    user_id = payload.get("sub")

    if user_id is None:
        raise UserCreditialsException

    user = db.get(User, user_id)

    if user is None:
        raise UserNotFoundException

    return user