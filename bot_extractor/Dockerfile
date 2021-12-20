FROM python:3
COPY . /usr/src/app
COPY requirements.txt /usr/src/app/requirements.txt
WORKDIR /usr/src/app
RUN pip install -r requirements.txt
CMD ["gunicorn"  , "-b", "0.0.0.0:5000", "bot:app"]