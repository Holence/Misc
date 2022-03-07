import re
import xml.dom.minidom

with open("fraidycat.opml","r",encoding="utf-8") as f:
    xml_string=f.read()
dom = xml.dom.minidom.parseString(xml_string)
pretty_xml_as_string = dom.toprettyxml()

opml=pretty_xml_as_string.split("\n")

# def printText():
#     for i in range(5,10):
#         print(text[i])

rss_dict={}
for i in range(len(opml)):
    t=opml[i]
    if "bandcamp.com" in t:
        continue
    if "twitter.com" in t:
        continue
    if "category" in t:
        tag=re.findall("(?<=category=\").*?(?=\")",t)[0]
        t=re.sub(" category=\".*?\"","",t)
        if "," in tag:
            tag=tag[tag.find(",")+1:]
            # print(tag)
        else:
            tag="Home"
        if rss_dict.get(tag)==None:
            rss_dict[tag]=[t]
        else:
            rss_dict[tag].append(t)

new_opml="\n".join(opml[:7])+"\n"
for tag in rss_dict.keys():
    new_opml+="\t\t<outline text=\"%s\" title=\"%s\">\n"%(tag,tag)
    for feed in rss_dict[tag]:
        new_opml+="\t"+feed+"\n"
new_opml+="\n".join(opml[-3:])

with open("output_fraidycat.opml",'w',encoding="utf-8") as f:
    f.write(new_opml)