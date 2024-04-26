# import json
# import subprocess
# import csv
# import time



# # Function to run maze generation and return the runtime
# runtime =0
# def generate_maze_runtime(json_files):
#     total_runtime = 0
#     for json_file in json_files:
#         command = ["python3", "mazeTester.py", json_file]
#         start_time = time.time()
#         process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#         print(process.stdout.decode())
#         end_time = time.time()
#         runtime = end_time - start_time
#         total_runtime += runtime
#         print(json_file, ":", runtime, "seconds")
       
#         if process.returncode != 0:
#             print("Error:", process.stderr.decode())
#         storeRuntime(json_file, runtime)
#     return total_runtime



# # Generate maze runtime for each JSON file
# # with open("runtimes_list.csv", mode='w', newline='') as file:
# #         writer = csv.writer(file)
# #         writer.writerow(["Rows * Columns", "Runtime (seconds)"])
# # for i in range(num_files):
# #     json_file = f"sampleConfig_list{i + 1}.json"
# #     runtime = generate_maze_runtime(json_file)
# def storeRuntime(runTime, filename, jsonFileName, rowNum, colNum):
#     with open(filename, mode='a', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow([jsonFileName, f"{rowNum} * {colNum}", runTime])


# with open("runtimes_Vert.csv", mode='w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["JSONFileName", "Rows * Columns", "Runtime (seconds)"])
    
# def storeRuntime(runTime, filename, jsonFileName, rowNum, colNum):
#     with open(filename, mode='a', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow([jsonFileName, rowNum*colNum , runTime])
# j = 0
# k = 0
# l = 0
# density_levels = [25, 50, 75]

# # Generate and save maze configurations for each density level

# while j < 3:
#     json_files = [f"sampleConfig_list_density_{density}_{i + 1}.json" for density in [25, 50, 75] for i in range(3)]
#     runtime = generate_maze_runtime(json_files)
#     j += 1
  





# # Output runtimes to a CSV file
# # print("Maze Runtimes: ", testerRunTime)
# # with open("maze_runtimes.csv", "w", newline="") as csv_file:
# #     writer = csv.writer(csv_file)
# #     writer.writerow(["Total Rows * Columns", "Runtime (seconds)"])
# #     for i, runtime in enumerate(testerRunTime):
# #         with open(f"sampleConfig_list{i + 1}.json", "r") as json_file:
# #             data = json.load(json_file)
# #             rows = data["rowNum"]
# #             columns = data["colNum"]
# #             ColumnRows = rows * columns
# #         writer.writerow([ColumnRows, testerRunTime[i]])


#         #use this in maze tester to get the runtime of the maze no need big lengthy code

import json
import subprocess
import csv
import time

# Function to run maze generation and return the runtime
def generate_maze_runtime(json_files):
    total_runtime = 0
    for json_file in json_files:
        command = ["python", "mazeTester.py", json_file]
        start_time = time.time()
        process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        end_time = time.time()
        runtime = end_time - start_time
        total_runtime += runtime
        print(json_file, ":", runtime, "seconds")
        if process.returncode != 0:
            print("Error:", process.stderr.decode())
        # Get JSON file information
        with open(json_file, 'r') as f:
            json_data = json.load(f)
            rowNum = json_data['rowNum']
            colNum = json_data['colNum']
            jsonFileName = json_file
        # Store runtime information
        storeRuntime(runtime, "Array_density.csv", jsonFileName, rowNum, colNum)
    return total_runtime

# Function to store runtime information in a CSV file
def storeRuntime(runTime, filename, jsonFileName, rowNum, colNum):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([jsonFileName, f"{rowNum} * {colNum}", runTime])

# Initialize CSV file
with open("Array_density.csv", mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["JSONFileName", "Rows * Columns", "Runtime (seconds)"])

# Generate and save maze configurations for each density level
density_levels = [25, 50, 75]

for _ in range(3):  # Repeat the process 3 times
    for density in density_levels:
        
        json_files = [f"sampleConfig_array_density_{density}_{i + 1}.json" for i in range(3)]
        generate_maze_runtime(json_files)
