FROM python:3

WORKDIR /usr/local/app
COPY app.py .
RUN pip3 install Flask requests

EXPOSE 80
ENTRYPOINT python3 app.py