from lxml import etree

xmlread = etree.parse("show_security_zones.xml")
myxml = xmlread.getroot()

for each in myxml.findall(".//zones-security"):
    print(each.find(".//zones-security-zonename").text)
