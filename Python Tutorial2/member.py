"""
membership operator = used to test weather a variable is found in a sequence (string, list, touple, set, dictionary)
in or not in
"""
word = "apple"
letter = input("Enter a character or substring: ")
if letter in word:
    print("Found")
else:
    print("Not found")

student = {"Tanvir", "Foyez", "Asif"}
name = input("Enter a name: ")
if name not in student:
    print("Not Found")
else:
    print("Found")

grades = {"Tanvir": "A-", "Foyez":"A+", "Asif":"A"}
student = input("Enter a name: ")
if student in grades:
    print(f"{student}'s grade = {grades[student]}")
else:
    print("Not found")

