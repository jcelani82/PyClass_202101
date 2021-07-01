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


