#!/usr/bin/env python
import xml.dom.minidom
doc = xml.dom.minidom.parse("zad17_xml_parser_save.xml")


#Tylko DOM może zapisywać do pliku, dlatego wybieram opcję DOM

print(doc.nodeName)
print(doc.firstChild.tagName)
supply = doc.getElementsByTagName("supply")
for s in supply:
    print(s.getAttribute("name"))

newsupply = doc.createElement("supply")
newsupply.setAttribute("name", "Weapon")
doc.firstChild.appendChild(newsupply)
xml_string = doc.toxml()
save_path_file = "zad17_xml_parser_save.xml"
  
with open(save_path_file, "w") as f: 
    f.write(xml_string)  