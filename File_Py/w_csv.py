import json
import csv

employee = [
    ["Name", "Age", "Job"], 
    ["Tanvir", 23, "Engineer"], 
    ["Naieem", 22, "Administrator"], 
    ["Mabud Ali", 24, "Doctor"]
]
file_path = "w_csv.csv"
try:
    with open(file_path, "w") as file:
        writer = csv.writer(file)
        for row in employee:
            writer.writerow(row)
        print("Done")
except FileExistsError:
    print("Not founded")