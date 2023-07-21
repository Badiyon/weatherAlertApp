FROM python:latest

WORKDIR /app

RUN pip install requests

COPY . . /app/

CMD ["python", "weatherAlertAppMain.py"]