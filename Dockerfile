FROM python:3.11-alpine
LABEL project='telephone-book'

WORKDIR /book

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . /book

CMD [ "python", "start.py" ]