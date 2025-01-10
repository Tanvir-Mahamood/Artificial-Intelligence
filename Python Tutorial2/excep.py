"""
exception = an event that interrupts the flow of a program
            (divide by 0, type error, value error)
            1. try, 2. except, 3.finally
"""

try:
    number = int(input("Enter a number:"))
    print(1 / number)
except ZeroDivisionError:
    print("Cannot divide by 0")
except ValueError:
    print("Number only")
except Exception:
    print("Something went wrong")
finally:
    print("Do some cean up here")