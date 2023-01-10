FROM node:19.4-slim 

WORKDIR /app
  
# commons start  
RUN apt-get update \
    && apt-get install -y libpq-dev gcc openssl \
    && rm -rf /var/lib/apt/lists/* 


COPY package.json package.json
RUN npm install
RUN npm install -g @angular/cli

COPY . .
RUN chmod +x start-reload.sh

RUN ng build
