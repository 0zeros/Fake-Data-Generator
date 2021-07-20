from data_generator import *


# will print all elements of list
def print_list(list_of_items):
    for item in list_of_items:
        print(item)


# set parameters to generate list of phone numbers
format = "+1 xxx-yyy-zzzz"

element = ["xxx","yyy","zzzz"]

constraints = {"xxx": {"type": "integer", "length": "3" },
               "yyy": {"type": "integer", "length": "3"},
               "zzzz": {"type": "integer", "length": "4"}
               }

data_sets = {}

# call generator function and print the list which is returned by generator
print_list(data_generator(100, format, element, constraints, data_sets))
