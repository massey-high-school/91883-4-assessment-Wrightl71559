# component 3 - create equations
# get user input and use it to generate questions

# imports random
import random

# integer checking function
def intcheck(question, low, high):
    valid = False
    error = ("Please enter an integer")
    while not valid:
       try:
            response = int(input(question))

            if low <= response <= high:
                return response
            else:
                print("That integer is either too low or too high")
                print()
       except ValueError:
           print(error)
           print()


# string checking function (made by Miss Gottschalk)
def string_checker(question, to_check):
    valid = False
    while not valid:

        response = input(question).lower()

        for item in to_check:
            if response == item:
                return response
            elif response == item[0]:
                return item

        print("Please enter a or b")


# Main Routine

q_options = ["a", "b"]
q_type = string_checker("for square root questions enter <a> or for squaring questions enter <b>  ", q_options)

q_number = intcheck("How many questions would you like? (up to 10)  ", 1, 10)

q_subject = random.randint(1,15)

for item in q_number:
    if q_type == "a":
        square_root = q_subject * q_subject
        u_answer = input("What is the square root of {}?  ".format(square_root))
    else:
        u_answer = input("what is {} squared?  ".format(q_subject))
        



