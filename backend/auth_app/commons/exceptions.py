from enum import Enum
from fastapi import HTTPException, status


from sqlalchemy.exc import IntegrityError
 

# sqlalchemy Exception -- start  
    # IntegrityError  == Wraps a DB-API IntegrityError
# sqlalchemy Exception -- end



# sqlalchemy Exception -- start  
    #  errors.lookup('23505')    === UniqueViolation
# sqlalchemy Exception -- end


# jose Exception -- start  
from jose.exceptions import ExpiredSignatureError, JWTError
# jose Exception -- end


class psycopg2_Exceptions(str, Enum):
    # https://www.postgresql.org/docs/9.2/errcodes-appendix.html
    not_null_violation =                            "23502" 
    foreign_key_violation =                         "23503"
    UniqueViolation =                               "23505"
 

def Get_psycopg2_Exceptions_details(ex:Exception):
    try:
        pgcode = ex.orig.pgcode
    except:
        print("Exception Name : ", ex.__class__.__name__)
        print("Exception  : ", str(ex))
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, "HTTP_500_INTERNAL_SERVER_ERROR") 

    if pgcode:
        if psycopg2_Exceptions.foreign_key_violation == pgcode :
            raise HTTPException(status.HTTP_400_BAD_REQUEST, str(ex).splitlines()[0])
        if psycopg2_Exceptions.not_null_violation == pgcode:
            raise HTTPException(status.HTTP_400_BAD_REQUEST, str(ex).splitlines()[0])
        if psycopg2_Exceptions.UniqueViolation == pgcode:
            raise HTTPException(status.HTTP_409_CONFLICT, str(ex).splitlines()[0])
        else:
            pgcode = pgcode
            # add error dont forget !! 

def Get_jose_exceptions(ex:Exception):
    cls_name = ex.__class__.__name__
    if cls_name == "JWTError": 
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Token is invalid")
    elif cls_name == "ExpiredSignatureError":
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "ExpiredSignatureError")   




def Get_Exceptions_details(ex:Exception):
     
    # try to find Exceptions in ...
    Get_jose_exceptions(ex)
    Get_psycopg2_Exceptions_details(ex) 

    # if not found will raise HTTP_500_INTERNAL_SERVER_ERROR !!
    print("Exception Name : ", ex.__class__.__name__)
    print("Exception  : ", str(ex))
    raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, "HTTP_500_INTERNAL_SERVER_ERROR") 

class CustomException_1(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="custom details HTTP_429_TOO_MANY_REQUESTS !!!!!",
        )


