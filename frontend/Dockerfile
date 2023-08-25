FROM node:lts-alpine

# for prod
# RUN npm install -g http-server

WORKDIR /app
COPY package.json .
RUN npm install
COPY . .

# for prod
#RUN npm run build

EXPOSE 8080

# production
#CMD [ "http-server", "dist"]

# development
CMD ["npm", "run", "serve"]
