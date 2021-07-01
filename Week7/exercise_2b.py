import xmltodict

xmlfile = open("show_security_zones.xml")
xmlread = xmlfile.read().strip()
xmldata = xmltodict.parse(xmlread)


print()
print("Part 2a")
print(xmldata)
print(type(xmldata))

print()
print("Part 2b")
for zone in enumerate(xmldata['zones-information']['zones-security']):
    print(f"Security Zone #{zone[0]}: {zone[1]['zones-security-zonename']}")

