from string_format_generator import *


# will print all elements of list
def print_list(list_of_items):
    for item in list_of_items:
        print(item)

# set parameters to generate list of full name ids
format = "fname mname lname"

element = ["fname","mname","lname"]

constraints = {"fname": '{"choose": "fname list"}',    "mname": '{"choose": "mname list"}',    "lname": '{"choose": "lname list"}'}

data_sets = {
    "fname list": ["Kenneth", "Daniel", "Richard"],
    "mname list": ["John", "Ronald", "George"],
    "lname list": ["Christopher", "David", "James"]
}

# call generator function and print the list which is returned by generator
print_list(string_format_generator(100, format, element, constraints, data_sets))