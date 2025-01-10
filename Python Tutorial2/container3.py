groceries = [["apple", "orange", "banana", "coconut"], ["celery", "carrots", "potatoes"], ["chicken", "fish", "turkey"]]
print(groceries)
print(groceries[1])
print(groceries[1][0])

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()

num_pad = ((1,2,3), (4,5,6), (7,8,9), ("*", 0, "#"))
for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()


# quiz game
questions = ("ques1", "ques2", "ques3", "ques4", "ques5")
options = (("a aa", "b ss", "c dd", "d ff"), 
           ("a gg", "b hh", "c ii", "d jj"), 
           ("a kk", "b ll", "c zz", "d xx"), 
           ("a yy", "b cc", "c vv", "d bb"), 
           ("a nn", "b mm", "c qq", "d ww"))

answers = ("a", "b", "c", "d", "e")
guesses = []
score = 0
question_no = 0

for question in questions:
    print("---------------")
    print(question_no+1,".", question)
    for option in options[question_no]:
        print(option)
    guess = input("Enter (a, b, c, d)").lower()
    guesses.append(guess)
    if(guess == answers[question_no]):
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(answers[question_no], "is the correct answer")
    question_no += 1

print("====================")

print("Answers:", end=" ")
for answer in answers:
    print(answer, end=" ")
print()

print("Guess:", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

score = (score / len(questions)) * 100
print(f"Your score: {score:.2f}%")