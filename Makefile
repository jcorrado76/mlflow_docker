build:
	docker build -t mlflow_server .

serve:
	docker run -p 5000:5000 mlflow_server

env:
	conda env create --file environment.yml

generate_env_yml:
	conda env export --name mlflow_env > environment.yml
