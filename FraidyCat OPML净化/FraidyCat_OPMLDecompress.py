import xml.dom.minidom

with open("fraidycat.opml","r",encoding="utf-8") as f:
    xml_string=f.read()
dom = xml.dom.minidom.parseString(xml_string)
pretty_xml_as_string = dom.toprettyxml()

with open("output_fraidycat.opml","w",encoding="utf-8") as f:
    f.write(pretty_xml_as_string)