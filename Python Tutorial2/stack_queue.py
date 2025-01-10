# stack
books = []
books.append("C")
books.append("C++")
books.append("Python")
print("books.top() : ", books[-1])
books.pop()
print("books.top() : ", books[-1])
books.pop()
books.pop()

if not books:
    print("No pop and top operation. Stack is empty.")
else:
    books.pop()



# queue
from collections import deque
bank = deque(["Tanvir", "Mahamood", "Dipe"])
print(bank)
bank.popleft()
print(bank)