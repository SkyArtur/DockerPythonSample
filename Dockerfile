FROM ubuntu:22.04
LABEL maintainer='SkyArtur <sky_artur@hotmail.com>'
WORKDIR /app
COPY . .
RUN apt update && apt upgrade -y && \
    apt install python3 python3-dev python3-venv python3-pip -y
CMD [ "python3", "main.py" ]
