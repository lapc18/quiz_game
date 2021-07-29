from classes import Question

questions = [Question("""\nWhat is the color of the sky?
                       \na) Red b) Blue c) Yellow""", "BLUE"),
             Question("""\nWhat is the color of the grass?
                       \na) Green b) Purple c) Black""", "GREEN"),
             Question("""\nHow many fingers do humans have on each hand?
                       \na) 2 b) 4 c) 5""", "5")
             ]
points = 0
for item in questions:
    print(item.prompt)
    user_answer = input("\nAnswer: ")
    if user_answer.upper() == item.answer:
        points += 1
    else:
        points = points
print(f"\nYou got {points} points.")
