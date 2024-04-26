
import json
import random

def generate_maze_data_list_density(density):
    
    #use a do while loop to get the same random number of rows and columns
    rows = 50
    cols= 50
    total_cells = rows * cols
    num_obstacles = int(total_cells * (density / 100))
    maze = [[0] * cols for _ in range(rows)]
    obstacles_placed = 0 

    while( obstacles_placed < num_obstacles):
        row = random.randint(0, rows - 1)
        col = random.randint(0, cols - 1)
        entrance_1 = [-1, random.randint(0, cols-1)]
        entrance_2 = [random.randint(0, rows-1), -1]
        exit_1 = [random.randint(0, rows-1), cols]
        exit_2 = [rows, random.randint(0, cols-1)]
        if maze[row][col] == 0:
            maze[row][col] = 1
            obstacles_placed += 1

    
    # Create a dictionary representing the maze data
    maze_data = {
        "dataStructure": "adjlist",
        "rowNum": rows,
        "colNum": cols,
        "entrances": [entrance_1, entrance_2],
        "exits": [exit_1, exit_2],
        "generator": "recur",
        "visualise": True
    }
    return maze_data

def generate_maze_data_adjMat_density(density):

    rows = 50
    cols = 50
    total_cells = rows * cols
    num_obstacles = int(total_cells * (density / 100))
    maze = [[0] * cols for _ in range(rows)]
    obstacles_placed = 0 

    while( obstacles_placed < num_obstacles):
        row = random.randint(0, rows - 1)
        col = random.randint(0, cols - 1)
        entrance_1 = [-1, random.randint(0, cols-1)]
        entrance_2 = [random.randint(0, rows-1), -1]
        exit_1 = [random.randint(0, rows-1), cols]
        exit_2 = [rows, random.randint(0, cols-1)]
        if maze[row][col] == 0:
            maze[row][col] = 1
            obstacles_placed += 1
    
    # Create a dictionary representing the maze data
    maze_data = {
        "dataStructure": "adjmat",
        "rowNum": rows,
        "colNum": cols,
        "entrances": [entrance_1, entrance_2],
        "exits": [exit_1, exit_2],
        "generator": "recur",
        "visualise": True
    }
    return maze_data

def generate_maze_data_array_density(density):
    
    rows = 50
    cols = 50
    total_cells = rows * cols
    num_obstacles = int(total_cells * (density / 100))
    maze = [[0] * cols for _ in range(rows)]
    obstacles_placed = 0 

    while( obstacles_placed < num_obstacles):
        row = random.randint(0, rows - 1)
        col = random.randint(0, cols - 1)
        
        entrance_1 = [-1, random.randint(0, cols-1)]
        entrance_2 = [random.randint(0, rows-1), -1]
        exit_1 = [random.randint(0, rows-1), cols]
        exit_2 = [rows, random.randint(0, cols-1)]
        if maze[row][col] == 0:
            maze[row][col] = 1
            obstacles_placed += 1
    
    # Create a dictionary representing the maze data
    maze_data = {
        "dataStructure": "array",
        "rowNum": rows,
        "colNum": cols,
        "entrances": [entrance_1, entrance_2],
        "exits": [exit_1, exit_2],
        "generator": "recur",
        "visualise": True
    }
    return maze_data


import json
import random

def generate_maze_data_list_size(rows,cols):
    
    #use a do while loop to get the same random number of rows and columns
    
    total_cells = rows * cols
    num_obstacles = int(total_cells * (0.5))
    maze = [[0] * cols for _ in range(rows)]
    obstacles_placed = 0 

    while( obstacles_placed < num_obstacles):
        row = random.randint(0, rows - 1)
        col = random.randint(0, cols - 1)
        entrance_1 = [-1, random.randint(0, cols-1)]
        entrance_2 = [random.randint(0, rows-1), -1]
        exit_1 = [random.randint(0, rows-1), cols]
        exit_2 = [rows, random.randint(0, cols-1)]
        if maze[row][col] == 0:
            maze[row][col] = 1
            obstacles_placed += 1

    
    # Create a dictionary representing the maze data
    maze_data = {
        "dataStructure": "adjlist",
        "rowNum": rows,
        "colNum": cols,
        "entrances": [entrance_1, entrance_2],
        "exits": [exit_1, exit_2],
        "generator": "recur",
        "visualise": True
    }
    return maze_data

def generate_maze_data_adjMat_size(rows,cols):

    
    total_cells = rows * cols
    num_obstacles = int(total_cells * (0.5))
    maze = [[0] * cols for _ in range(rows)]
    obstacles_placed = 0 

    while( obstacles_placed < num_obstacles):
        row = random.randint(0, rows - 1)
        col = random.randint(0, cols - 1)
        entrance_1 = [-1, random.randint(0, cols-1)]
        entrance_2 = [random.randint(0, rows-1), -1]
        exit_1 = [random.randint(0, rows-1), cols]
        exit_2 = [rows, random.randint(0, cols-1)]
        if maze[row][col] == 0:
            maze[row][col] = 1
            obstacles_placed += 1
    
    # Create a dictionary representing the maze data
    maze_data = {
        "dataStructure": "adjmat",
        "rowNum": rows,
        "colNum": cols,
        "entrances": [entrance_1, entrance_2],
        "exits": [exit_1, exit_2],
        "generator": "recur",
        "visualise": True
    }
    return maze_data

def generate_maze_data_array_size(rows,cols):
    
    rows = 50
    cols = 50
    total_cells = rows * cols
    num_obstacles = int(total_cells * (0.5))
    maze = [[0] * cols for _ in range(rows)]
    obstacles_placed = 0 

    while( obstacles_placed < num_obstacles):
        row = random.randint(0, rows - 1)
        col = random.randint(0, cols - 1)
        
        entrance_1 = [-1, random.randint(0, cols-1)]
        entrance_2 = [random.randint(0, rows-1), -1]
        exit_1 = [random.randint(0, rows-1), cols]
        exit_2 = [rows, random.randint(0, cols-1)]
        if maze[row][col] == 0:
            maze[row][col] = 1
            obstacles_placed += 1
    
    # Create a dictionary representing the maze data
    maze_data = {
        "dataStructure": "array",
        "rowNum": rows,
        "colNum": cols,
        "entrances": [entrance_1, entrance_2],
        "exits": [exit_1, exit_2],
        "generator": "recur",
        "visualise": True
    }
    return maze_data

#no of JSON files to generate 

#no of JSON files to generate 

density_levels = [25, 50, 75]

# Generate and save maze configurations for each density level
for density in density_levels:
    for i in range(3):  # Generate three samples for each density level
        maze_data = generate_maze_data_list_density(density)
        file_path = f"sampleConfig_list_density_{density}_{i + 1}.json"
        with open(file_path, "w") as json_file:
            json.dump(maze_data, json_file, indent=2)

for density in density_levels:
    for i in range(3):  # Generate three samples for each density level
        maze_data = generate_maze_data_adjMat_density(density)
        file_path = f"sampleConfig_mat_density_{density}_{i + 1}.json"
        with open(file_path, "w") as json_file:
            json.dump(maze_data, json_file, indent=2)

for density in density_levels:
    for i in range(3):  # Generate three samples for each density level
        maze_data = generate_maze_data_array_density(density)
        file_path = f"sampleConfig_array_density_{density}_{i + 1}.json"
        with open(file_path, "w") as json_file:
            json.dump(maze_data, json_file, indent=2)
            



sizes = [(5, 5), (50, 50), (100, 100)]
for size in sizes:
    rows, cols = size
    for i in range(3):  # Generate three samples for each size
        maze_data = generate_maze_data_list_size(rows, cols)
        file_path = f"sampleConfig_list_size_{rows}x{cols}_{i + 1}.json"
        with open(file_path, "w") as json_file:
            json.dump(maze_data, json_file, indent=2)
            
for size in sizes:
    rows, cols = size
    for i in range(3):  # Generate three samples for each size
        maze_data = generate_maze_data_adjMat_size(rows,cols)
        file_path = f"sampleConfig_mat_size_{rows}x{cols}_{i + 1}.json"
        with open(file_path, "w") as json_file:
            json.dump(maze_data, json_file, indent=2)
            
for size in sizes:
    rows, cols = size
    for i in range(3):  # Generate three samples for each size
        maze_data = generate_maze_data_adjMat_size(rows,cols)
        file_path = f"sampleConfig_array_size_{rows}x{cols}_{i + 1}.json"
        with open(file_path, "w") as json_file:
            json.dump(maze_data, json_file, indent=2)



















