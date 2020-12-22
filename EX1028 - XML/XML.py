# -*- coding: utf-8 -*-
"""

<messages>
  <message type="machine">
    <time>10/21/2020 2:10:02 AM</time>
    <messageString>V02 88030233 00000000 1 00000000 00000000 00000001 BasicSupply.MachinePressure</messageString>
  </message>
  <message type="machine">
    <time>10/21/2020 2:13:56 AM</time>
    <messageString>V02 88d90024 00000000 1 00000002 00000000 00000004 0 1 4 1 1 8 Indexer</messageString>
  </message>
</messages>
"""

import xml.etree.ElementTree as ET

tree = ET.parse("15_10_2020.msh")
root = tree.getroot()

print (root.tag)
for child in root:
    print (child.tag, child.attrib)
    for grandson in child:
        if grandson.tag == "time":
            print(grandson.text)
