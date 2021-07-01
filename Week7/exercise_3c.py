import xmltodict
from pprint import pprint

def convertxml (xfile):

    xmlfile = open(xfile)
    xmlread = xmlfile.read().strip()
    xmldata = xmltodict.parse(xmlread, force_list={'zones-security'})
    return xmldata

if __name__ == "__main__" :

    xml_file = "show_security_zones_single_trust.xml"
    
    single_trust = convertxml(xml_file)
    print(type(single_trust['zones-information']['zones-security']))
