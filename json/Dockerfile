FROM node:18.7.0

WORKDIR /code

COPY package.json package.json
RUN npm install
RUN npm install -g json-server

COPY . .