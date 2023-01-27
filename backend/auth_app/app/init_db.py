import psycopg2 
import time
import sys , os 

from app.config import config

print("start psycopg2.connect  ....  ")
reconnect = 5
conn = None 
while True:
    try:
        print("========== start psycopg2.connect  ....  ")
        conn = psycopg2.connect(
        dbname='',
        user=os.environ.get('POSTGRES_USER'),
        password=os.environ.get('POSTGRES_PASSWORD'),
        host=os.environ.get('DB_HOST'),
        port=os.environ.get('DB_PORT') 
        )
        print("========== psycopg2.connect pass :) ")
        break
    except Exception as e:
        print(e)
        print(f"reconnect: {reconnect}")
        time.sleep(1)
        reconnect -= 1
        if reconnect == 0:
            break 
print("========== start psycopg2.connect  done :)  ")




APP_NAME = config.APP_NAME
DB_NAME = config.DB_NAME


if conn is not None:
    conn.autocommit = True

    # Creating a cursor object using the cursor() method
    cursor = conn.cursor() 

    try:
        # Creating a database
        cursor.execute(f'CREATE database {DB_NAME}')
        print(f"Database {DB_NAME} created successfully........")
    # if the database already exist ignore
    except Exception:
        print(f"Database {DB_NAME} already there........")

    # Closing the connection
    conn.close()
else:
    print("failed to connect to db")


print("running migration for app ",APP_NAME," --- START ")   
os.chdir(f"./{APP_NAME}")
os.system("alembic upgrade head")
print("running migration for the app",APP_NAME," --- END ") 

 
