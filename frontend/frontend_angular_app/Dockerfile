FROM node:19.4.0-slim

WORKDIR /app

RUN npm install http-server -g
COPY dist dist
COPY start-reload.sh start-reload.sh
