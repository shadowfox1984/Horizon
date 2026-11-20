# src/infrastructure/security/jwt_handler.py
from datetime import datetime, timedelta
from typing import Optional
import jwt
from src.infrastructure.config import settings

class JWTHandler:
    ACCESS_TOKEN_EXPIRE_MINUTES = 15
    
    @staticmethod
    def create_access_token(profile_id: str) -> str:
        expire = datetime.utcnow() + timedelta(minutes=JWTHandler.ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode = {"sub": str(profile_id), "exp": expire}
        return jwt.encode(to_encode, settings.jwt_secret, algorithm="HS256")

    @staticmethod
    def decode_token(token: str) -> Optional[dict]:
        try:
            return jwt.decode(token, settings.jwt_secret, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None