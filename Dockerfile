FROM python:alpine

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

CMD ["python3", "-m", "shift_light"]