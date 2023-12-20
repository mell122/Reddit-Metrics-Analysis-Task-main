FROM python:3.11-bullseye
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY src .

RUN cd src

CMD [ "python3", "scraper.py"]