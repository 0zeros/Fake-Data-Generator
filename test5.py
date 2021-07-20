from data_generator import *


# will print all elements of list
def print_list(list_of_items):
    for item in list_of_items:
        print(item)


# set parameters to generate list of full name ids
format = "fname mname lname, xxxxxxxxxxxxxxxx, yyy, DD/MM/YYYY"

element = ["fname", "mname", "lname", "xxxxxxxxxxxxxxxx", "yyy", "DD", "MM", "YYYY"]

constraints = {"fname": {"type": "string", "choose": "fname list"},
               "mname": {"type": "string", "choose": "mname list"},
               "lname": {"type": "string", "choose": "lname list"},
               "xxxxxxxxxxxxxxxx": {"type": "integer", "length": "16"},
               "yyy": {"type": "integer", "length": "3"},
               "DD": {"type": "integer", "range": [1, 31]},
               "MM": {"type": "integer", "range": [1, 12]},
               "YYYY": {"type": "integer", "length": "4"},
               }

data_sets = {
    "fname list": ["Kenneth", "Daniel", "Richard"],
    "mname list": ["John", "Ronald", "George"],
    "lname list": ["Christopher", "David", "James"]
}

# call generator function and print the list which is returned by generator
print_list(data_generator(100, format, element, constraints, data_sets))