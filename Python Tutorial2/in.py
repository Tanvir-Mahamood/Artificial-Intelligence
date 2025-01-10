"""
membership operators = used to test weather a value or variable is found in a sequence
(string, list, touple, set, dictionary)
in
not in
"""

word = "Apple"
letter = input("Enter a character:")
if letter in word:
    print("founded")
else:
    print("not founded")

grade = {"alice":"a", "bob":"b"}
student = input("enter name:")
if student in grade:
    print(f"{student}'s grade: {grade[student]}")
else:
    print("not found")