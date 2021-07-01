import json
from pprint import pprint

filename = "readfile_4.json"
with open(filename) as f:
    readdata = json.load(f)

new_dict = {}

for a_keys, a_values in readdata.items():
    if a_keys == "ipV4Neighbors":
        for nei_list in a_values:
            for nei_keys, nei_values in nei_list.items():
                if nei_keys == "hwAddress":
                    dict_value = nei_values
                if nei_keys =="address":
                    dict_key = nei_values
            new_dict.update({dict_key : dict_value})
print("")
print(new_dict)
print("")
