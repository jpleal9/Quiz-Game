# Dictionary for the multiple options

QUESTIONS = {
    "When was the last time the New England Patriors where Super Bowl champions?":[
        "2019","2020","2018","2017"],

    "What is the secret name of Batman?":[
        "Bruce Wayne","Peter Parker","Clark Kent","Tony Stark"],
    
    "Who pays the song Master of Puppets?":[
        "Metallica","Kate Bush","Queen","Pink Floyd"],

    "What's the name of Marshal Ericksen's father from How I Met Your Mother?":[
        "Marvin","Marshal","Marcus","Marcelus"]

}

for question,all_answers in QUESTIONS.items():
    correct_answer=all_answers[0]
    print(f"{question}")
    for one_answers in sorted(all_answers):
        print(f" -{one_answers}")
    answer = input("Your answer is...\n")

    if answer == correct_answer:
        print("Correct, you really now this stuff!\n--------------------")
    else:
        print(f"Nope, the answer is {correct_answer!r}\n--------------------")
    