# python writing files (.txt, .json, .csv)
# here only .txt

# mode = "W" : if the file exists, then overwrite it
# otherwise creates a new file and write it

# mode = "x": if the file exists, it does not touch it
# otherwise creates a new file and write it

# mode = "a": similar as "w" except overwriting 
"""
txt_data = "I love Tonuza"
# file_path = "output.txt"
file_path = "C:/Users/Lenovo/OneDrive/Desktop/new.txt"

with open(file_path, "w") as file:
    file.write(txt_data)
    print(f"Writing completed at '{file_path}'")

"""

"""
txt_data = "I love Tonuza"
file_path = "C:/Users/Lenovo/OneDrive/Desktop/new.txt"

try:
    with open(file_path, "x") as file:
        file.write(txt_data)
        print(f"Writing completed at '{file_path}'")
except FileExistsError:
    print("File aready exist")
"""

"""
txt_data = "I love Tonuza"
file_path = "output.txt"

with open(file_path, "a") as file:
    file.write("\n" + txt_data)
    print(f"Writing completed at '{file_path}'")
"""

employee = ["Tanvir", "Jihad", "Arafat"]
file_path = "employee.txt"
with open(file_path, "w") as file:
    for people in employee:
        file.write(people + " ")
