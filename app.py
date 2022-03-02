import os
import jwt


class Token:
    def __init__(self) -> None:
        self.__secret = os.environ.get("SECRET", "secret")
        self.__algorithm = os.environ.get("ALGORITHM", "HS256")

    def create_token(self, data: dict) -> str:
        return jwt.encode(payload=data, key=self.__secret, algorithm=self.__algorithm)

    def decode_token(self, token: str) -> dict:
        return jwt.decode(jwt=token, key=self.__secret, algorithms=[self.__algorithm])
