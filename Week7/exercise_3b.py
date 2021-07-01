import xmltodict
from pprint import pprint

def convertxml (xfile):

    xmlfile = open(xfile)
    xmlread = xmlfile.read().strip()
    xmldata = xmltodict.parse(xmlread)
    return xmldata

if __name__ == "__main__" :

    xmlfiles = [
        "show_security_zones.xml",
        "show_seccurity_zones_single_trust.xml"
    ]

    output = []
    
    for xfile in xmlfiles:
        output.append(convertxml(xfile))

    for xml in output:
#        print()
#        pprint(xml)
#        print(type(xml))
#        print()
        print()
        print(xml)
        print()
        print(type(xml['zones-information']))
        print(type(xml['zones-information']['zones-security']))
        print()
