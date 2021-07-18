from string_format_generator import *


# will print all elements of list
def print_list(list_of_items):
    for item in list_of_items:
        print(item)


# set parameters to generate list of email ids
format = "str1@str2.str3"

element = ["str1","str2","str3"]

constraints = {"str1": '{"random": "10"}',    "str2": '{"random": "5"}',    "str3": '{"choose": "domain list"}'}

data_sets = {
    "domain list": ["com", "edu", "co", "pk"]
}

# call generator function and print the list which is returned by generator
print_list(string_format_generator(100, format, element, constraints, data_sets))