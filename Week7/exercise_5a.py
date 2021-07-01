from pprint import pprint
from lxml import etree

xmlread = etree.parse("show_version.xml")
xmldata = xmlread.getroot()

print()
print(xmldata.tag)
print()
print(xmldata.nsmap)
print()
print(etree.tostring(xmldata).decode())
print()
