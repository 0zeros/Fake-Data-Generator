import json
import re
from integer_generator import *


def number_format_generator(number_of_rows, format, elements, constraints):
    output = []
    for i in range(number_of_rows):
        clone_format = format
        for element in elements:
            ele_con = constraints[element]
            con = json.loads(ele_con)
            con_item = con.items()
            for key, value in con_item:
                if key == "range":
                    clone_format = re.sub(element, str(integer_between(value[0], value[1])), clone_format)
                elif key == "length":
                    clone_format = re.sub(element, str(integer_of_length(int(value))), clone_format)
        output.append(clone_format)
    return output
