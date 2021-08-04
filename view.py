import json
import pandas as pd


def view():
    fileObj = open("output.json", "r")
    temp = fileObj.read()
    out = json.loads(temp)
    dataframe = pd.DataFrame.from_dict(out)
    print(dataframe)
