# component 2
# create list for both types of question
# import random

# imports random
import random

# main code
# number to square
s_questions = ["3", "6", "9", "12", "10", "7", "11", "15", "5", "8"]


# generates random from list
for item in range(1, 20):
    random_1 = random.choice(s_questions)
    print(random_1, end="\t")


