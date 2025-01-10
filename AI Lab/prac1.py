a = "abc 'gg' gg'g gg\'g gg \" !#?"
b = "abcdefghijklmnop"
print(a)
print(b[3:10:2])
a = 'd'
print(type(a))
print(type(b[3:10:2]))

b = [1,2,3,4,5,6,7,8,9]
c = b[2::2]
print(type(c))


# string
str = "abcdcaba"
print(str.capitalize())
print(str.count("ab"))
print(str.startswith("ad"))
print(str.endswith("ba"))

str2 = "I am {name} and I am {year} old"
print(str2.format(name="Tanvir", year=22))
print(str.isalpha())
print(str.isspace())

myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)

myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"
x = mySeparator.join(myDict)
print(x)
print(type(x))

txt = "hello, my name is Peter, I am 26 years old"
print(txt.split())
print(txt.split(","))
print(txt.split(",",1))

txt = "(hello!) "
cleaned_txt = txt.strip("()! ") 
print(cleaned_txt)

ttxt = [' How', ' ara ', "you,", "sir?"]
