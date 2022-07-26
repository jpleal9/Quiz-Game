# Dictionary with enumerate

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

for question,alternatives in QUESTIONS.items():
    correct_answer = alternatives[0]
    sorted_alternatives = sorted(alternatives)
    print(f"{question}")
    for label, alternative in enumerate(sorted_alternatives):
        print(f" {label}) {alternative}")

    answer_label = int(input(f"Your answer is... \n"))
    answer = sorted_alternatives[answer_label]
    if answer == correct_answer:
        print("That is correct!!! \n--------------------")
    else:
        print(f"Unfortunatelly the answer is {correct_answer!r}\n--------------------")
