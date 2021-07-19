from number_format_generator import *


# will print all elements of list
def print_list(list_of_items):
    for item in list_of_items:
        print(item)


# set parameters to generate list of date
format = "DD/MM/YYYY"

element = ["DD","MM","YYYY"]

constraints = {"DD": '{"range": [1,31] }',    "MM": '{"range": [1,12]}',    "YYYY": '{"length": "4"}'}


# call generator function and print the list which is returned by generator
print_list(number_format_generator(100, format, element, constraints))