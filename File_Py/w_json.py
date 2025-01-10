import json
employee = {
    "name": "Tanvir",
    "age": 23,
    "job": "student"
}
file_path = "w_json.json"
try:
    with open(file_path, "w") as file:
        json.dump(employee, file, indent=4)
        print("JSON has written")
except FileExistsError:
    print("Not found")