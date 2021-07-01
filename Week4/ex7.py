import textfsm
from pprint import pprint

template_file = "ex2template.template"
template = open(template_file)

with open("ex2data.txt") as f:
    show_int_status = f.read()

re_table = textfsm.TextFSM(template)
data = re_table.ParseText(show_int_status)
template.close()

new_dict = {}
f_list = []

for record in data:
    new_dict.update({"DUPLEX" : record[4]})    
    new_dict.update({"PORT_NAME" : record[0]})    
    new_dict.update({"PORT_TYPE" : record[5]})    
    new_dict.update({"SPEED" : record[3]})    
    new_dict.update({"STATUS" : record[1]})    
    new_dict.update({"VLAN" : record[2]})    

    f_list.append(new_dict)

print(f_list)
    

