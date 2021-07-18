import json
import re
from choose_random import *
from random_string_generator import *


def string_format_generator(number_of_rows, format, string_element, constraints, data_sets):
    output = []
    for i in range(number_of_rows):
        clone_format = format
        for element in string_element:
            ele_con = constraints[element]
            con = json.loads(ele_con)
            con_item = con.items()
            for key, value in con_item:
                if key == "choose":
                    clone_format = re.sub(element, choose_random(data_sets[value]), clone_format)
                elif key == "random":
                    clone_format = re.sub(element, string_of_length(int(value)), clone_format)
        output.append(clone_format)
    return output
