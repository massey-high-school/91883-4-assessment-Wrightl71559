# component 6 - statement generator function
# implement statement generating function from previous code

# imports random
import random


# integer checking function
def intcheck(question, low, high):
    valid = False
    error = "Please enter an integer"
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


# statement generator function
def rps_statement(statement, char):
    print()
    print(char * len(statement))
    print(statement)
    print(char * len(statement))
    print

# Main Routine

q_options = ["a", "b"]
q_type = string_checker("For square root questions enter <a> or for squaring questions enter <b>  ", q_options)

q_number = intcheck("How many questions would you like? (up to 10)  ", 1, 10)
qs_asked = 0

while qs_asked != q_number:
    q_subject = 8
    qs_squared = q_subject * q_subject

    if q_type == "a":
        u_answer = intcheck("What is the square root of {}?  ".format(qs_squared), 1, 300)
    else:
        u_answer = intcheck("what is {} squared?  ".format(q_subject), 1, 300)

    if q_type == "a" and u_answer == q_subject:
        print("That is correct !!")
    elif q_type == "a"and u_answer != q_subject:
        print("Sorry, that is incorrect. The answer is {}".format(q_subject))
    elif q_type == "b" and u_answer == qs_squared:
        print("That is correct !!")
    else:
        print("Sorry, that is incorrect. that answer is {}".format(qs_squared))

    qs_asked += 1
