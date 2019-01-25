FROM python:alpine3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
RUN chmod -R a+x /app/
CMD python ./src/index.py
