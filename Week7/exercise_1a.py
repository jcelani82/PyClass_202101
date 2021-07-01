import xml.etree.ElementTree as etree

xmlfile = open("xml_1a.xml")
xmlread = xmlfile.read().strip()
xmldata = etree.fromstring(xmlread.strip())

print(xmldata)
print(type(xmldata))


