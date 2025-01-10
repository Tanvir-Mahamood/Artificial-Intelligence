# read file

file_path1 = "r_file.txt"
try:
    with open(file_path1, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("not found")
except PermissionError:
    print("You do not have permission to read the file")




file_path2 = "w_json.json"
try:
    with open(file_path2, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("not found")
except PermissionError:
    print("You do not have permission to read the file")




file_path3 = "w_csv.csv"
try:
    with open(file_path3, "r") as file:
        content = file.read()
        for line in content:
            print(line)
        # print(content)
except FileNotFoundError:
    print("not found")
except PermissionError:
    print("You do not have permission to read the file")