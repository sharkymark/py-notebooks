import numpy as np
import time
import os

# Grid size
GRID_SIZE = 75

def random_grid(size):
    """Generate a random grid of 0s and 1s."""
    return np.random.choice([0, 1], size=(size, size), p=[0.8, 0.2])

def update(grid):
    """Compute next generation based on Game of Life rules."""
    new_grid = grid.copy()
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            # Count live neighbors
            neighbors = sum([
                grid[i, (j-1) % GRID_SIZE], grid[i, (j+1) % GRID_SIZE],  # Left & Right
                grid[(i-1) % GRID_SIZE, j], grid[(i+1) % GRID_SIZE, j],  # Top & Bottom
                grid[(i-1) % GRID_SIZE, (j-1) % GRID_SIZE],  # Top Left
                grid[(i-1) % GRID_SIZE, (j+1) % GRID_SIZE],  # Top Right
                grid[(i+1) % GRID_SIZE, (j-1) % GRID_SIZE],  # Bottom Left
                grid[(i+1) % GRID_SIZE, (j+1) % GRID_SIZE]   # Bottom Right
            ])
            
            # Apply Conway's rules
            if grid[i, j] == 1 and (neighbors < 2 or neighbors > 3):
                new_grid[i, j] = 0  # Dies
            elif grid[i, j] == 0 and neighbors == 3:
                new_grid[i, j] = 1  # Becomes alive
    
    return new_grid

def print_grid(grid):
    """Print the grid to the terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen for smooth updating
    for row in grid:
        print("".join("█" if cell else " " for cell in row))  # Block for alive cells, space for dead cells

# Initialize grid
grid = random_grid(GRID_SIZE)

# Run continuously
try:
    while True:
        print_grid(grid)
        grid = update(grid)
        time.sleep(0.1)  # Adjust speed (lower = faster)
except KeyboardInterrupt:
    print("\nGame of Life stopped.")
