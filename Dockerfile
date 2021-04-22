FROM python:3.8.2-slim

RUN pip install mlflow

WORKDIR /mlflow

EXPOSE 5000

ENTRYPOINT [ "mlflow", "server", "--host", "0.0.0.0", "-p", "5000"]
