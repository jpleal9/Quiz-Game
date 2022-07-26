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
    
    "Who pays the song Master of Puppets?":[
        "Metallica","Kate Bush","Queen","Pink Floyd"],

    "What's the name of Marshal Ericksen's father from How I Met Your Mother?":[
        "Marvin","Marshal","Marcus","Marcellus"]

}

#Now we will preprocess the data so it is ready for our quiz

def prepare_questions(questions,num_questions):
    num_questions = min(num_questions,len(questions)) #Checks what is the minimum between the number
    # questions we want (num_questions) and the total number of questions in the script
    return random.sample(list(questions.items()),k=num_questions) #Returns the sample list of all the
    # questions that will be featured on the script



