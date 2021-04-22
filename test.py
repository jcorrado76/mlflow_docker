#!/usr/bin/env conda run -n mlflow_env python

import os
from random import randint
import argparse
import mlflow

# if you changed the port number in the Makefile, you need to change it here as
# well
PORT = "5000"

if __name__ == "__main__":
    # if you've deployed the MLFlow server to a remote server, you need
    # to change this value to be the Public IPv4 of your remote server
    HOSTNAME = "0.0.0.0"
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", type=str, default=HOSTNAME)

    args = parser.parse_args()

    HOSTNAME = args.host
    mlflow.set_tracking_uri(f"http://{HOSTNAME}:{PORT}")
    mlflow.log_param("param1", randint(0, 100))

    client = mlflow.tracking.MlflowClient()
    data = client.get_run(mlflow.active_run().info.run_id).to_dictionary()
    print(data)
