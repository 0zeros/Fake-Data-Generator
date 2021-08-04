import re
from choose_random import *
from random_string_generator import *
from integer_generator import *
import os
import json


def data_generator(dataField, number_of_rows, format, string_element, constraints, data_sets):
    output = []
    if os.path.isfile("output.json"):
        fileObj = open("output.json", "r")
        t = fileObj.read()
        fileData = json.loads(t)
        fileObj.close()
    else:
        fileData = {}
    for i in range(number_of_rows):
        clone_format = format
        for element in string_element:
            ele_con = constraints[element]
            con_keys = list(ele_con)
            if ele_con[con_keys[0]] == "yes":
                record_name = ele_con["name"]
                data_list = fileData[record_name]
                clone_format = re.sub(element, data_list[i], clone_format)
            elif ele_con[con_keys[0]] == "no":
                if ele_con[con_keys[1]] == "string":
                    if con_keys[2] == "choose":
                        clone_format = re.sub(element, choose_random(data_sets[ele_con[con_keys[2]]]), clone_format)
                    elif con_keys[2] == "random":
                        clone_format = re.sub(element, string_of_length(int(ele_con[con_keys[2]])), clone_format)
                elif ele_con[con_keys[1]] == "integer":
                    if con_keys[2] == "range":
                        clone_format = re.sub(element, str(integer_between(ele_con[con_keys[2]][0], ele_con[con_keys[2]][1])), clone_format)
                    elif con_keys[2] == "length":
                        clone_format = re.sub(element, str(integer_of_length(int(ele_con[con_keys[2]]))), clone_format)
        output.append(clone_format)
    fileObj = open("output.json", "w")
    temp_pair = {dataField: output}
    fileData.update(temp_pair)
    fileObj.write(json.dumps(fileData))
    fileObj.close()
