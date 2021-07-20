from data_generator import *


# will print all elements of list
def print_list(list_of_items):
    for item in list_of_items:
        print(item)


# set parameters to generate list of date
format = "DD-MM-YYYY"

element = ["DD","MM","YYYY"]

constraints = {"DD": {"type": "integer", "range": [1, 31]},
               "MM": {"type": "integer", "range": [1, 12]},
               "YYYY": {"type": "integer", "length": "4"}
               }

data_sets = {}

# call generator function and print the list which is returned by generator
print_list(data_generator(100, format, element, constraints,data_sets))