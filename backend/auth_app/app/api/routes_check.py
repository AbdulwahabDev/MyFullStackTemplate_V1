from fastapi import HTTPException, status

from app.common.dependencies import db_session
from fastapi import APIRouter


test_router = APIRouter(prefix="", tags=["test"])

 

@test_router.get("/test")
def ts_connection(db_session=db_session):
    """
    فقط لإختبار الاتصال 
    """
    
    return "Hello world ... :)"