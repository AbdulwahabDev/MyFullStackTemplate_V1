from fastapi import HTTPException, status


class CustomException_1(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="custom details HTTP_429_TOO_MANY_REQUESTS !!!!!",
        )
