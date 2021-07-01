import xml.etree.ElementTree as etree

xmlfile = open("xml_1a.xml")
xmlread = xmlfile.read().strip()
xmldata = etree.fromstring(xmlread.strip())


print()
print("Part 1a")
print(xmldata)
print(type(xmldata))

print()
print("Part 1b")
print(etree.tostring(xmldata).decode())

print()
print("Part 1c")
print(xmldata.tag)
print(len(xmldata))

print()
print("Part 1d")
first_child = xmldata.getchildren()[0]
print(first_child.tag)

