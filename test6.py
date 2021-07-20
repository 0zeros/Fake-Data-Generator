from data_generator import *


# will print all elements of list
def print_list(list_of_items):
    for item in list_of_items:
        print(item)


# set parameters to generate list of addresses
format = "Street # xx, city, state, country"

element = ["xx", "city", "state", "country"]

constraints = {"xx": {"type": "integer", "range": [1, 100]},
               "city": {"type": "string", "choose": "city list"},
               "state": {"type": "string", "choose": "state list"},
               "country": {"type": "string", "choose": "country list"}
               }

data_sets = {
    "city list": ["New York", "Los Angeles", "Chicago", "Miami"],
    "state list": ["California","Illinois","Florida","Texas"],
    "country list": ["USA", "Pakistan"]
}

# call generator function and print the list which is returned by generator
print_list(data_generator(100, format, element, constraints, data_sets))