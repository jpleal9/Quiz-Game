# Add variety to my quiz

import random
from string import ascii_lowercase

NUM_QUESTIONS_PER_QUIZ = 5
QUESTIONS = {
    "When was the last time the New England Patriots where Super Bowl champions?":[
        "2019","2020","2018","2017"],

    "What is the secret name of Batman?":[
        "Bruce Wayne","Peter Parker","Clark Kent","Tony Stark"],
    
    "Who pays the song Master of Puppets?":[
        "Metallica","Kate Bush","Queen","Pink Floyd"],

    "What's the name of Marshal Ericksen's father from How I Met Your Mother?":[
        "Marvin","Marshal","Marcus","Marcellus"]

}

num_questions = min(NUM_QUESTIONS_PER_QUIZ, len(QUESTIONS))
questions = random.sample(list(QUESTIONS.items()), k = num_questions) #This will give the number of questions
#for the quiz, which will be the minimum between the total questions and the NUM_QUESTIONS_PER_QUIZ


num_correct = 0
for num, (question,alternatives) in enumerate(questions, start=1): #The num helps to keep track of the question number
    print(f"\nQuestion {num}:")
    print(f"{question}")
    correct_answer = alternatives[0]
    labeled_alternatives = dict(zip(ascii_lowercase,random.sample(alternatives,k=len(alternatives)))) 
    #Creates a dictionary with the sequence of answers by question, now using the new method
    #The random is a different way to use the sorted
    for label, alternative in labeled_alternatives.items():
        print(f" {label}) {alternative}")
    
    while(answer_label := input("\nYour answer is...")) not in labeled_alternatives:
        #The while cycle will keep the input correct, between the 4 possible answers
        print(f"Please answer one of {', '.join(labeled_alternatives)}")
        #The print will re-question for it to be on the valid input

    answer = labeled_alternatives[answer_label] #The input
    if answer == correct_answer:
        print("⭐That is correct!!⭐\n------------------------------\n")
        num_correct +=1
    else:
        print(f"😭Unfortunately the answer is {correct_answer!r}😭\n------------------------------\n")

print(f"\nYour score is {num_correct} in {num} questions!\n")

if num_correct == 4: #This one is my own, a way to give a final message to the quiz
    print("Amazing job! You really are a force to be reckoned!\n\n-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")
elif num_correct in range(2,4):
    print("Good job, but there is room for improvement!\n\n-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")
else:
    print("Man you suck, try again!\n\n-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")