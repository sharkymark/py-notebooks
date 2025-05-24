# Jupyter Notebook playground

## Run the app

### from source
`cd` into the repo directory and run the app

```sh
jupyter lab --IdentityProvider.token='' --ip='*' --port=8888 --allow-root --no-browser
```

or add the VS Code extension for Jupyter Notebooks and run the app from there.

### from dev container

The dev container automatically starts the app with `"postCreateCommand": "jupyter lab --IdentityProvider.token='' --ip='*' --port=8888 --allow-root --no-browser"`

## Dev Container

Notice the `Dockerfile` and `devcontainer.json` which uses a slim Python container image in the Dockerfile, and passes the Coder authentication environment variables into the dev container.

This approach frees you up from having a specific Python version and module on your local machine e.g., Mac and let the dev container set all of this up. You do still need to set the environment variables locally which is more secure and better than putting into the repo with .gitignore. ☠️


## Virtual Environment

If not using a dev container, it's recommended to create a virtual environment first to isolate your dependencies:

```sh
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

## Jupyter

Pull up the .ipynb file in your favorite editor (e.g., VS Code) and run the notebook. 

## Packages

After activating your virtual environment, install the required packages with:

```sh
pip install -r requirements.txt
```
