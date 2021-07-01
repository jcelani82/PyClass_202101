from lxml import etree

xmlread = etree.parse("show_security_zones.xml")
myxml = xmlread.getroot()

print()
print("Find tag of the first zones-security-zonename element")
print("--------------------------")
print(myxml.find(".//zones-security/zones-security-zonename").text)
print()

