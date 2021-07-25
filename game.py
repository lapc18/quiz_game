questions = [
                "1) What is the color of the sky?\na) Red  b) Blue  c) Yellow",
                "2) What is the color of the grass?\na) Green  b) Purple  c) Black",
                "3) How many fingers do humans have on each hand?\na) 2  b) 4  c) 5"
            ]
answers =   [
                "Blue",
                "Green",
                "5"
            ]
            

points = 0
for question in questions:
    print(question)
    user_answer = input("\nAnswer: ")
    if user_answer in answers:
        points += 1
    else:
        points = points
print(f"You got {points} points.")
