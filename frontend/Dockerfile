FROM python:3.10-slim AS production

# ARG APP_NAME=frontend_app

WORKDIR /app
  
# commons start  
RUN apt-get update \
    && apt-get install -y libpq-dev gcc openssl \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir --upgrade pip 

COPY commons/requirements.txt commons/requirements.txt
RUN  pip install --no-cache-dir -r commons/requirements.txt


COPY commons commons 

COPY ProjectConfig.py ProjectConfig.py

COPY start-reload.sh start-reload.sh
RUN chmod +x start-reload.sh


COPY dockerfiles/requirements.txt $APP_NAME/requirements.txt
RUN  pip install --no-cache-dir -r $APP_NAME/requirements.txt

COPY . .


 