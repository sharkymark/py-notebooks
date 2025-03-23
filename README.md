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

If not using a dev container, you will to `pip install -r requirements.txt` to install the required packages:

# Game of Life

This project implements Conway's Game of Life using Python. The Game of Life is a cellular automaton devised by the mathematician John Horton Conway in 1970. It consists of a grid of cells that can live, die, or multiply based on a few mathematical rules.

## Rules

1. Any live cell with fewer than two live neighbors dies, as if by underpopulation.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

## Files

### `game_of_life.py`

This script runs the Game of Life simulation. It includes the following functions:

- `random_grid(size)`: Generates a random grid of 0s and 1s.
- `update(grid)`: Computes the next generation of the grid based on the Game of Life rules.
- `print_grid(grid)`: Prints the grid to the terminal.

The script initializes a random grid and continuously updates and prints it until interrupted by the user.

## Running the Simulation

To run the simulation, execute the following command in your terminal:

```sh
python game_of_life.py
```

Press `Ctrl+C` to stop the simulation.

# Factorial CLI App

This CLI app demonstrates recursion by calculating the factorial of a given number.

### Purpose

The purpose of this program is to provide a simple example of how recursion can be used to solve problems in Python. It takes an integer as input and calculates its factorial using a recursive function.

### Usage

To use the CLI app, run the following command:

```sh
python factorial.py <number>
```

Replace `<number>` with the integer you want to calculate the factorial for.

### Example

```sh
python factorial.py 5
```

This will output:

```
The factorial of 5 is 120
```