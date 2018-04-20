FROM python:3

WORKDIR /usr/local/app
COPY app.py .
RUN pip install Flask requests

EXPOSE 80
ENTRYPOINT python app.py