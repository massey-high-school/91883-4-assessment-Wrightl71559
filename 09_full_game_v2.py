# Full game
# make necessary adjustments

# imports random
import random


# integer checking function
def intcheck(question, low, high, error_2):
    valid = False
    error = "Please enter an integer"
    while not valid:
       try:
            response = int(input(question))

            if low <= response <= high:
                return response
            else:
                print()
                print(error_2)
                print()
       except ValueError:
           print()
           print(error)
           print()


# string checking function (made by Miss Gottschalk)
def string_checker(question, to_check, error):
    valid = False
    while not valid:

        print()
        response = input(question).lower()
        print()

        for item in to_check:
            if response == item:
                return response
            elif response == item[0]:
                return item

        print(error)


# statement generator function
def pa_statement(statement, char):
    print()
    print(char * len(statement))
    print(statement)
    print(char * len(statement))
    print()

# Main Routine
# quiz title
pa_statement("** Squares & Square Roots **", "*")

# intro - if user has played before instructions aren't given and vice versa
y_n = ["yes", "no"]
game_intro = string_checker("Have you played this game before? (yes or no)  ", y_n, "Please enter yes or no")

if game_intro == "no":
    print()
    print("This maths quiz is about squaring and square rooting.")
    print("- You will be asked which type of questions you’d like and how many you want. ")
    print("- Try your best to figure out the correct answer. ")
    print("- If you are incorrect the correct answer will be shown to you.")
    print("- Your game statistics will be shown at the end of the game.")
    print("Good Luck!")
    print()

# loops entire game
play_again = ""
while play_again == "":

    game_stats = []
    correct_answers = 0

    # get input - what type of question and how many
    q_options = ["root", "square"]
    q_type = string_checker("For square root questions enter <r or root> or for squaring questions"
                            " enter <s or square>  ", q_options, "Please enter square or root")

    q_number = intcheck("How many questions would you like? (up to 10)  ", 1, 10,
                        "Please enter an integer between 1 and 10")
    # loops game to provide amount of questions specified by user
    qs_asked = 0
    print()
    while qs_asked != q_number:
        # generates random for squaring questions and number for square root questions
        q_subject = random.randint(1, 15)
        qs_squared = q_subject * q_subject

        # generates question based on user input
        if q_type == "root":
            u_question = "What is the square root of {}?  ".format(qs_squared)
            u_answer = intcheck("{}".format(u_question), 1, 10000, "Please enter an integer greater than zero")
        else:
            u_question = "what is {} squared?  ".format(q_subject)
            u_answer = intcheck("{}".format(u_question), 1, 10000, "Please enter an integer greater than zero")

        # compares user answer to correct answer
        if q_type == "root" and u_answer == q_subject:
            pa_statement("!! That is correct !!", "!")
            feedback = "Correct"
        elif q_type == "root"and u_answer != q_subject:
            pa_statement("== Sorry, that is incorrect. The answer is {} ==".format(q_subject), "=")
            feedback = "Incorrect"
        elif q_type == "square" and u_answer == qs_squared:
            pa_statement("!! That is correct !!", "!")
            feedback = "Correct"
        else:
            pa_statement("== Sorry, that is incorrect. The answer is {} ==".format(qs_squared), "=")
            feedback = "Incorrect"

        # counts questions asked
        qs_asked += 1
        # records questions and results for game stats
        q_result = "Q{} - {}Your answer: {}  > {} <".format(qs_asked, u_question, u_answer, feedback)
        game_stats.append(q_result)
        if feedback == "Correct":
            correct_answers += 1

    # displays game stats - question, users answer, correct or incorrect
    print()
    print("## Game Statistics ##")

    for item in game_stats:
        print(item)
    print("You answered {}/{} questions correct".format(correct_answers, q_number))

# end game mechanics
    print()
    play_again = input("Press <enter> to play again or any key to quit  ")

print()
print("Thank you for playing :)")
