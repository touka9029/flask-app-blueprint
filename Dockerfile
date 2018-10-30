FROM python:3.6.7-alpine3.7

WORKDIR /www

COPY flaskr/ .
RUN pip install -r requirements.txt

CMD [ "python", "app.py" ]
