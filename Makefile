build:
	docker build -t mlflow_server .

serve:
	docker run -p 5000:5000 mlflow_server
