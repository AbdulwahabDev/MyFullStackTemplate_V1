
FROM python:3.10-slim AS production


WORKDIR /app
  
# commons start 

RUN apt-get update \
    && apt-get install -y libpq-dev gcc openssl \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir --upgrade pip 

COPY commons/requirements.txt commons/requirements.txt
RUN  pip install --no-cache-dir -r commons/requirements.txt


COPY commons commons
COPY init_db.py init_db.py
COPY start-reload.sh start-reload.sh
RUN chmod +x ./start-reload.sh 
# commons end 


COPY app/init_db.py app/init_db.py 
 
# app requirements
COPY app/requirements.txt app/requirements.txt
RUN  pip install --no-cache-dir -r app/requirements.txt
# app requirements
 

COPY app app
COPY .env .env