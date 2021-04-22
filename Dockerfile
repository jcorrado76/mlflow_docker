FROM python:3.8.2-slim

RUN pip install mlflow

WORKDIR /mlflow

EXPOSE 5000

CMD [ "mlflow", "server" ]
