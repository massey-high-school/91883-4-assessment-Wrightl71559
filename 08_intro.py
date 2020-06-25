# component 8 - write intro
# ask user if they have played game before
# if yes start game
# if no display game introduction / instructions

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


# main code
pa_statement("** Maths Quiz **", "*")

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


print()
print("For square root questions enter <a> or for squaring questions enter <b>")
