FROM python:3.8-alpine
# RUN apt-get update && apt-get install -y install python3

EXPOSE 5000
WORKDIR /app
COPY . /app
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

CMD ["python" , "wsgi.py" ]