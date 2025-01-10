# python file detection
# relative file path or absolute file path

# relative file path:

import os

# file_path = "test.txt"
# file_path = "C:/Users/Lenovo/OneDrive/Desktop/Cppfile.cpp"
file_path = "C:/Users/Lenovo/OneDrive"
if os.path.exists(file_path):
    print("Path found")
    if os.path.isfile(file_path):
        print("It is a file")
    elif os.path.isdir(file_path):
        print("It is a directory")
else:
    print("Path not found")