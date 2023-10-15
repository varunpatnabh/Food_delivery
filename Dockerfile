FROM python:3.9

ENV FLASK_APP=app/app.py

RUN mkdir /project
WORKDIR /project

COPY . .
RUN pip3 install -r ./requirements.txt

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]