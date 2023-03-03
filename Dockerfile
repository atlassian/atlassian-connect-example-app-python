FROM python:3.7

COPY . /app
WORKDIR /app

RUN python3 -m pip install --upgrade pip

COPY requirements.txt requirements.txt

RUN pip3 install python-dotenv
RUN pip3 install -r requirements.txt

COPY . .
CMD [ "python3", "app.py" ]
