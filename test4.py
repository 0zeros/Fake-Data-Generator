from number_format_generator import *


# will print all elements of list
def print_list(list_of_items):
    for item in list_of_items:
        print(item)


# set parameters to generate list of phone numbers
format = "+1 xxx-yyy-zzzz"

element = ["xxx","yyy","zzzz"]

constraints = {"xxx": '{"length": "3" }',    "yyy": '{"length": "3"}',    "zzzz": '{"length": "4"}'}


# call generator function and print the list which is returned by generator
print_list(number_format_generator(100, format, element, constraints))


# card holder name, card number, cvc, expiry date
# street # number, city, state, country
