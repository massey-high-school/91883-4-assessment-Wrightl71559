# component 1 b - get input

# put in integer checking function from previous code
# set up question to ask user
# return user input


# integer checking function
def intcheck(question, low, high):
    valid = False
    error = ("Please enter an integer between 1 and 10 (inclusive)")
    while not valid:
       try:
            response = int(input(question))

            if low <= response <= high:
                return response
            else:
                print(error)
                print()
       except ValueError:
           print(error)


# Main Routine
q_number = intcheck("How many questions would you like? (up to 10)  ", 1, 10)
print(q_number)
