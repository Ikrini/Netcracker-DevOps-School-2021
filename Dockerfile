FROM python:3.7

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

#ENV PORT 8080
#ENV HOST 0.0.0.0

RUN pip install aiogram
RUN pip install chatterbot
RUN pip install bottle
RUN pip install flask

ADD requirements.txt /

#COPY requirements.txt /. .
#RUN pip install -r requirements.txt
#RUN pip install  aiogram ChatterBot

COPY . .

EXPOSE 8080

ENTRYPOINT ["python"]

#EXPOSE 8080

CMD ["main.py", "--host", "0.0.0.0", "-p", "8080"]

