#Lists option

QUESTIONS = [("When was the last time the New England Patriors where Super Bowl champions?","2019"),
("What is the secret name of Batman?","Bruce Wayne"),
("Who pays the song Master of Puppets?","Metallica")]

for question,result in QUESTIONS:
    answer = input(f"{question}\n")
    if answer == result:
        print("Correct! Ten points to Gryffindor!")
    else:
        print(f"Oh geez, {answer!r} is not the correct answer, but {result!r} is...")