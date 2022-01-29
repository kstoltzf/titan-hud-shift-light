FROM python:3.9.10-slim-buster

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

CMD ["python3", "-m", "shift_light"]