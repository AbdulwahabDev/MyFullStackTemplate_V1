from fastapi import Depends, Response
from sqlalchemy.orm import Session
 


def get_db_session_dependency(SessionLocal):
    def get_db_session():
        session: Session = SessionLocal()
        try:
            with session.begin():
                yield session
        finally:
            session.close()

    return get_db_session

 

 
