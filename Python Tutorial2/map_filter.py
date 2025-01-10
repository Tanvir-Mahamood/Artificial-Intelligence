def square(x):
    return x*x

num = [1, 2, 3, 4, 5]
result = list(map(square, num))
print(result)

result2 = list(filter(lambda x: x%2==0, num))
print(result2)

# list comprehensive
result3 = [x*x for x in num]
print(result3)

result4 = [x for x in num if x%2==0]
print(result4)

#zip function
roll = [62,63,64,65]
name=["Tanvir", "Foyez", "Asif", "Shifat"]
print(list(zip(roll, name, "abcd")))