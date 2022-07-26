# Improving the layout of the app with more structured stuff

from string import ascii_lowercase

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

for num, (question,alternatives) in enumerate(QUESTIONS.items(), start=1): #The num helps to keep track of the question number
    print(f"\nQuestion {num}:")
    print(f"{question}")
    correct_answer = alternatives[0]
    labeled_alternatives = dict(zip(ascii_lowercase, sorted(alternatives))) #Creates a dictionary with the sequence of answers by question
    for label, alternative in labeled_alternatives.items():
        print(f" {label}) {alternative}")

    answer_label = input(f"\nYour answer is...")
    answer = labeled_alternatives.get(answer_label) #The input
    if answer == correct_answer:
        print("⭐That is correct!!⭐ \n--------------------")
    else:
        print(f"😭Unfortunatelly the answer is {correct_answer!r}😭\n--------------------")