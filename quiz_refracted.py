# This will be used to refract the code in a more organized way and with the use
# of functions

import random
from string import ascii_lowercase

NUM_QUESTIONS_PER_QUIZ = 5
QUESTIONS = {
    "When was the last time the New England Patriots where Super Bowl champions?":[
        "2019","2020","2018","2017"],

    "What is the secret name of Batman?":[
        "Bruce Wayne","Peter Parker","Clark Kent","Tony Stark"],
    
    "Who plays the song Master of Puppets?":[
        "Metallica","Kate Bush","Queen","Pink Floyd"],

    "What's the name of Marshal Ericksen's father from How I Met Your Mother?":[
        "Marvin","Marshal","Marcus","Marcellus"],

    "Kratos is the main character of what video game series?":[
        "God of War","Pokemon","Horizon Zero Dawn","Stranded"],

    "Who plays Hannibal in the Silence of the Lambs movie?":[
        "Anthony Hopkins","Morgan Freeman","Michael Caine","Sean Connery"],

    "What is the capital of Ireland?":[
        "Dublin","Galway","Cork","Waterford"],

    "Where did sushi originate?":[
        "China","Japan","Korea","India"],
    
    "What is a nargle?":[
        "I have no idea","A monster","A beast","A man"],

    "What is the symbol for potassium?":[
        "K","P","T","PT"],

    "Which infinity stone was located on Vormir?":[
        "Soul Stone","Time Stone","Mind Stone","Reality Stone"]

}

#Now we will preprocess the data so it is ready for our quiz

def prepare_questions(questions,num_questions):
    num_questions = min(num_questions,len(questions)) #Checks what is the minimum between the number
    # questions we want (num_questions) and the total number of questions in the script
    return random.sample(list(questions.items()),k=num_questions) #Returns the sample list of all the
    # questions that will be featured on the script

def get_answers(question,alternatives):
    print(f"{question}")
    labeled_alternatives = dict(zip(ascii_lowercase,alternatives))
    #Creates a dictionary with the sequence of answers by question, now using the new method
    for label, alternative in labeled_alternatives.items():
        print(f" {label}) {alternative}")
    
    while (answer_label := input("\nYour answer is...")) not in labeled_alternatives:
    #The while cycle will keep the input correct, between the 4 possible answers
        print(f"Please answer one of {', '.join(labeled_alternatives)}")
    #The print will re-question for it to be on the valid input

    return labeled_alternatives[answer_label]

def ask_question(question,alternatives):
    correct_answer = alternatives[0] #Because correct answer is always the first one
    ordered_alternatives = random.sample(alternatives, k = len(alternatives)) #Randomizes the possible answers

    answer = get_answers(question, ordered_alternatives)
    if answer == correct_answer:
        print("⭐That is correct!!⭐\n------------------------------\n")
        return 1
    else:
        print(f"😭Unfortunately the answer is {correct_answer!r}😭\n------------------------------\n")
        return 0

def run_quiz():
    questions = prepare_questions(QUESTIONS, num_questions = NUM_QUESTIONS_PER_QUIZ)

    num_correct = 0
    for num, (question,alternatives) in enumerate(questions, start = 1):
        print(f"\nQuestion {num}:")
        num_correct += ask_question(question, alternatives)
    
    print(f"\nYour score is {num_correct} in {num} questions!\n")

    if num_correct == 5: #This one is my own, a way to give a final message to the quiz depending on the
        # amount of right answers
        print("Amazing job! You really are a force to be reckoned!\n\n-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")
    elif num_correct in range(2,5):
        print("Good job, but there is room for improvement!\n\n-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")
    else:
        print("Man you suck, try again!\n\n-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")

if __name__ == "__main__": #This makes run_quiz() to run when we call the .py file, but not when we import
    # the file as a module
    run_quiz()