FROM python:3.8

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

#ENV PORT 8080
#ENV HOST 0.0.0.0

RUN pip install aiogram
RUN pip install numpy
RUN pip install nltk
RUN pip install h5py
RUN pip install tensorflow

ADD requirements.txt /

#COPY requirements.txt /. .
#RUN pip install -r requirements.txt
#RUN pip install  aiogram ChatterBot

COPY . /usr/src/app

EXPOSE 8080

ENTRYPOINT ["python"]

#EXPOSE 8080

CMD ["main.py", "--host", "0.0.0.0", "-p", "8080"]

