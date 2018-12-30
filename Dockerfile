FROM python:3-alpine

RUN apk add build-base python-dev py-pip jpeg-dev zlib-dev
ENV LIBRARY_PATH /lib:/usr/lib
RUN mkdir app
COPY . app/
RUN pip install ./app

# set up non-root user
#ARG user=dev
#ARG group=app
#WORKDIR /home/$user
#RUN addgroup -S $group && adduser -S -G $group $user
#USER $user:$group

