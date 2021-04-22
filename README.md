# Usage
This repo contains the Dockerfile, Makefile and test script to spin up an MLFlow tracking server inside a Docker container.

To build the docker image, run:
`make build`

To start the docker container, run:
`make serve`

Note that this tracking server is exposed on port 5000.

If you've started the docker container on your local machine, we can now move on to executing the `test.py` script.

First, you must have conda installed.
If you have conda installed, then you can just run:
`make env`

Note that this is going to create an environment called `mlflow_env` in your conda installation.

You don't need to activate it, as the appropriate execution is taken care of in the shebang line in the python script.

You can delete it when you're done with:
`conda env remove -n mlflow_env`

Finally, run the `test.py` script:
`chmod +x test.py`
`./test.py`

If it worked, you should now have a new run in your default experiment (labeled "0"), and you should see the output of the data from that run in your console.

# Deploy to Remote Server
If you have deployed this MLFlow server to a remote server (EC2 or something), then you'll need to specify the Public IPv4 address of that instance to your `test.py`.
The script is set up to take a value for host name as a command line argument, so the execution is like:
`./test.py --host [Public IPv4 here]`
# Change Port Number
If you want your MLFlow server to be accessible from a different port, you'd simply go into the Makefile, and change:

```
serve:
	docker run -p 5000:5000 mlflow_server
```

To:
```
serve:
	docker run -p {ENTER YOUR NEW PORT HERE}:5000 mlflow_server
```

And run:
`make serve`

Then, the MLFlow UI would be accessible at:
`http://[HOST]:[NEW PORT VALUE HERE]`

If you want to deploy this MLFlow server onto a remote server, you will need to change the host name as well.

