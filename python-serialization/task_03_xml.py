#!/usr/bin/env python3
"""Save Python data in an XML format and retrieve it later"""


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)
    return True


def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    result = {}
    for child in root:
        result[child.tag] = child.text

    return result
