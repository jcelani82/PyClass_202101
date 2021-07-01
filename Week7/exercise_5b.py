from pprint import pprint
from lxml import etree

xmlread = etree.parse("show_version.xml")
xmldata = xmlread.getroot()

print((xmldata.find(".//{*}proc_board_id")).text)

