FROM python:3.12.3


RUN pip install --upgrade pip
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
COPY ./stripe_test ./
RUN pip install gunicorn

