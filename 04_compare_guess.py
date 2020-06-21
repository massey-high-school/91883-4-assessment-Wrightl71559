# component 4 - compare guess
# set up program to compare user guess to correct answer using a simple equation
# give feedback (correct / not correct)

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
q_type = string_checker("For square root questions enter <a> or for squaring questions enter <b>  ", q_options)

q_number = intcheck("How many questions would you like? (up to 10)  ", 1, 10)

q_subject = 8
qs_squared = q_subject * q_subject

if q_type == "a":

    u_answer = intcheck ("What is the square root of {}?  ".format(qs_squared), 1, 300)
else:
    u_answer = intcheck ("what is {} squared?  ".format(q_subject), 1, 300)


if q_type == "a" and u_answer == q_subject:
    print("That is correct !!")
elif q_type == "a"and u_answer != q_subject:
    print("Sorry, that is incorrect. The answer is {}".format(q_subject))
elif q_type == "b" and u_answer == qs_squared:
