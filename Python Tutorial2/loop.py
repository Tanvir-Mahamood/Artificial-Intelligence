# name = input("Enter your name: ")
# while name == "":
#     print("You didn't enter name.")
#     name = input("Enter your name: ")
# print(f"Welcome {name}")

# for x in range(1, 11):
#     print(x)
# print("again")

# for x in range(1, 11, 2):
#     print(x)
# print("again")


import time

my_time = int(input("Enter the time in seconds: "))
for x in range(0, my_time):
    print(x)
    time.sleep(1)
print("Time up")

for x in reversed(range(0, my_time)):
    print(x)
    time.sleep(1)
print("Time up")

my_time = int(input("Enter the time in seconds: "))
for x in range(my_time, 0, -1):
    second = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{second:02}")
    time.sleep(1)
print("The")
