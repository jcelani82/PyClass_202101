import xmltodict

xmlfile = open("show_security_zones.xml")
xmlread = xmlfile.read().strip()
xmldata = xmltodict.parse(xmlread)


print()
print("Part 2a")
print(xmldata)
print(type(xmldata))

print()
print("Part 2b)

