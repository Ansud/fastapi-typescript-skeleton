FROM node:21-alpine as build-deps

WORKDIR /webapp

# Initialize packages
COPY package.json tsconfig.json yarn.lock /webapp/
RUN yarn install

# Build directory structure
COPY public /webapp/public
COPY src /webapp/src
RUN yarn build

FROM nginx:1.25.3-alpine
COPY --from=build-deps /webapp/build /usr/share/nginx/html

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
