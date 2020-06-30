# Full game
# put together all components and make sure it works as expected (debug accordingly)

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
def pa_statement(statement, char):
    print()
    print(char * len(statement))
    print(statement)
    print(char * len(statement))
    print()

# Main Routine
pa_statement("** Maths Quiz **", "*")

play_again = ""
while play_again == "":

    y_n = ["yes", "no"]
    game_intro = string_checker("Have you played this game before? (yes or no)  ", y_n)

    if game_intro == "no":
        print()
        print("This maths quiz is about squaring and square rooting.")
        print("You will be asked which type of questions you’d like and how many you want. ")
        print("Try your best to figure out the correct answer. ")
        print("If you are incorrect the correct answer will be shown to you.")
        print("Your game statistics will be shown at the end of the game.")
        print("Good Luck!")
        print()

    game_stats = []

    q_options = ["a", "b"]
    q_type = string_checker("For square root questions enter <a> or for squaring questions enter <b>  ", q_options)

    q_number = intcheck("How many questions would you like? (up to 10)  ", 1, 10)
    qs_asked = 0

    while qs_asked != q_number:
        q_subject = random.randint(1, 15)
        qs_squared = q_subject * q_subject

        if q_type == "a":
            u_answer = intcheck("What is the square root of {}?  ".format(qs_squared), 1, 300)
        else:
            u_answer = intcheck("what is {} squared?  ".format(q_subject), 1, 300)

        if q_type == "a" and u_answer == q_subject:
            pa_statement("!! That is correct !!", "!")
            feedback = "Correct"
        elif q_type == "a"and u_answer != q_subject:
            pa_statement("== Sorry, that is incorrect. The answer is {} ==".format(q_subject), "=")
            feedback = "Incorrect"
        elif q_type == "b" and u_answer == qs_squared:
            pa_statement("!! That is correct !!", "!")
            feedback = "Correct"
        else:
            pa_statement("== Sorry, that is incorrect. The answer is {} ==".format(qs_squared), "=")
            feedback = "Incorrect"

        qs_asked += 1
        q_result = "Question {}: {}".format(qs_asked, feedback)
        game_stats.append(q_result)

    print()
    print("## Game Statistics ##")

    for item in game_stats:
        print(item)

    print()
    play_again = input("Press <enter> to play again or any key to quit  ")

print()
print("Thank you for playing :)")
