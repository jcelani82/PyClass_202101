import json
from pprint import pprint

filename = "readfile_3.json"
with open(filename) as f:
    readdata = json.load(f)

ipv4_list = []
ipv6_list = []


## BREAKING DOWN THE DICTIONARIES
for x, y in readdata.items():
    a = (y.keys())

    for b in a:
        if b == "ipv4": #IPV4
            for c, d in y.items():
                if c == "ipv4":
                    for e, f in d.items():
                        for h, g in f.items():
                            new_entry = (f"{e} /{g}")
                            ipv4_list.append(new_entry)
                else: ##IPV6 IP'S
                    for e, f in d.items():
                        for h, g in f.items():
                            new_entry = (f"{e} /{g}")
                            ipv6_list.append(new_entry)                            

        else: #IPV6
            for c, d in y.items():
                if c == "ipv4":#MAKE SURE ITS NOT A IPV4
                    for e, f in d.items():
                        for h, g in f.items():
                            new_entry = (f"{e} /{g}")
                            ipv4_list.append(new_entry)
                else:#IPV6
                    for e, f in d.items():
                        for h, g in f.items():
                            new_entry = (f"{e} /{g}")
                            ipv6_list.append(new_entry)
                                


print(f"\n\nThe IPV4 IP's with Prefixes are:")
for x in ipv4_list:
    print(x)
print(f"\n\nThe IPV6 IP's with Prefixes are:")
for x in ipv6_list:
    print(x)

