# component 1 a - get input

# put in string checking function from miss gottschalk
# set up question to ask user
# return user input


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
print(q_type)