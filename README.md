# Jupyter Notebook pandas datasets example

This repo shows 3 sample Jupyter Notebooks and Python code.  

* generic.ipydb are generic Pandas commands to analyze datasets. e.g., number of rows, columns, column names, distribution of values in a column, read in a csv.

* bls.ipynb returns PPI and CPI information showing the delta from last month and last 12 months

* fred.ipynb returns Federal Reserve economic information. API_KEY must be added as environment variable. If using a Coder template, enter the key during workspace creation as a parameter.

* The sets folder has publicly available datasets used by the notebooks.

## Run the app

### from source
`cd` into the repo directory and run the app

```sh
jupyter lab --IdentityProvider.token='' --ip='*' --port=8888 --allow-root --no-browser
```

### from dev container

The dev container automatically starts the app with `"postCreateCommand": "jupyter lab --IdentityProvider.token='' --ip='*' --port=8888 --allow-root --no-browser"`

## Dev Container

Notice the `Dockerfile` and `devcontainer.json` which uses a slim Python container image in the Dockerfile, and passes the Coder authentication environment variables into the dev container.

This approach frees you up from having a specific Python version and module on your local machine e.g., Mac and let the dev container set all of this up. You do still need to set the environment variables locally which is more secure and better than putting into the repo with .gitignore. ☠️


## Packages

If not using a dev container, you will to `pip install` the following packages:

```sh
jupyterlab
jupyter-core
notebook
pandas
prettytable
```