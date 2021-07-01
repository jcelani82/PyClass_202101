from lxml import etree

xmlread = etree.parse("show_security_zones.xml")
myxml = xmlread.getroot()

print()
print("Find tag of the first zones-security element")
print("--------------------------")
print(myxml.find(".//zones-security").tag)
print()

print("Find tag of all child elements of the first zones-security element")
print("--------------------------")

for child in myxml.find(".//zones-security").getchildren():
    print(child.tag)
