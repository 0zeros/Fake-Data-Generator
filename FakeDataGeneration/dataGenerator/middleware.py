from dataGenerator.data_generator import data_generator
import json


def middleware(JSONobject):
    print(JSONobject)
    fields = JSONobject.keys()
    print(fields)
    generated_data = {}
    for i in fields:
        ouput = data_generator(int(JSONobject[i]["num_of_rows"]),JSONobject[i]["format"],JSONobject[i]["element"],JSONobject[i]["constraints"],JSONobject[i]["data_sets"])
        temp_pair = {i: ouput}
        generated_data.update(temp_pair)
    return generated_data