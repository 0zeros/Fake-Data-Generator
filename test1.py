from data_generator import *


# will print all elements of list
def print_list(list_of_items):
    for item in list_of_items:
        print(item)


# set parameters to generate list of email ids
format = "str1@str2.str3"

element = ["str1","str2","str3"]

constraints = {"str1": {"type": "string", "random": "10"},
               "str2": {"type": "string", "random": "5"},
               "str3": {"type": "string", "choose": "domain list"}
               }

data_sets = {
    "domain list": ["com", "edu", "co", "pk"]
}

# call generator function and print the list which is returned by generator
print_list(data_generator(100, format, element, constraints, data_sets))