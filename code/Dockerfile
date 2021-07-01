FROM python:3.8

RUN mkdir -p /usr/src/app

COPY requirements.txt /usr/src/app/requirements.txt

WORKDIR /usr/src/app

RUN pip install -r requirements.txt

COPY . /usr/src/app

EXPOSE 8080

ENTRYPOINT ["python"]

#EXPOSE 8080

CMD ["main.py", "--host", "0.0.0.0", "-p", "8080"]
