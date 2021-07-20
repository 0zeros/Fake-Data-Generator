import re
from choose_random import *
from random_string_generator import *
from integer_generator import *


def data_generator(number_of_rows, format, string_element, constraints, data_sets):
    output = []
    for i in range(number_of_rows):
        clone_format = format
        for element in string_element:
            ele_con = constraints[element]
            con_keys = list(ele_con)
            if ele_con[con_keys[0]] == "string":
                if con_keys[1] == "choose":
                    clone_format = re.sub(element, choose_random(data_sets[ele_con[con_keys[1]]]), clone_format)
                elif con_keys[1] == "random":
                    clone_format = re.sub(element, string_of_length(int(ele_con[con_keys[1]])), clone_format)
            elif ele_con[con_keys[0]] == "integer":
                if con_keys[1] == "range":
                    clone_format = re.sub(element, str(integer_between(ele_con[con_keys[1]][0], ele_con[con_keys[1]][1])), clone_format)
                elif con_keys[1] == "length":
                    clone_format = re.sub(element, str(integer_of_length(int(ele_con[con_keys[1]]))), clone_format)
        output.append(clone_format)
    return output
