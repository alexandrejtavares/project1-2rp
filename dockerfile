FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV TWORPTEST=true100%

CMD [ "python", "-u", "./main.py" ]