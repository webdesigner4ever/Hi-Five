FROM python:3.8.12

ENV PORT 80
ENV DEBUG "False"

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . .

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "__init__.py"]
