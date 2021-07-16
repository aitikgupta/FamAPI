FROM node:10.15-alpine

WORKDIR /client

COPY package.json ./

RUN apk add yarn
RUN yarn install
RUN yarn global add serve

COPY ./public ./public
COPY ./src ./src

EXPOSE 5000

CMD yarn build && serve -s build
