import xml.etree.ElementTree as ET

from packages.string_definitions import add_string_1, add_string_2, edit_string

import sys
import os


# Dictionary of target nodes and XML replacements
replacements = {
    "addition" : ("ListOfReferenceCoded", (add_string_1, add_string_2)),
    "modification" : ("BuyerParty", edit_string)
}




# Expands the input PATH to an Absolute PATH
def expand_path(rel_path):
    return os.path.abspath(rel_path)

# Loads the XML file and parses it into a Tree structure
def load_xml_file(target_file):
    abs_path = expand_path(target_file)
    tree = ET.parse(abs_path)
    root = tree.getroot()
    return root, tree


# Recursively visit the Tree
def tree_visit(node, replacements):
    for child in node:
        if child.tag == replacements["addition"][0]:
            try:
                # Add the two nodes separaterly due to how XML requires the structure of the portion of code to be added
                new_node_1 = ET.fromstring(replacements["addition"][1][0])
                new_node_2 = ET.fromstring(replacements["addition"][1][1])
            except Exception as e:
                print(" --> Failed to parse the string into xml node: addition")
                print(e)
                sys.exit(-1)
            child.append(new_node_1)
            child.append(new_node_2)
        if child.tag == replacements["modification"][0]:
            child.clear()
            try:
                new_node = ET.fromstring(replacements["modification"][1])
            except Exception as e:
                print(" --> Failed to parse the string into xml node: modification")
                sys.exit(-1)
            child.append(new_node)
        tree_visit(child, replacements)

# Prettify the XML file (fix indentation and spacing)
def prettify_xml(root):

    def indent(elem, level=0):
        """Recursively indent XML elements for pretty-printing."""
        i = "\n" + "    " * level
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "    "
            for child in elem:
                indent(child, level + 1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i
    # Apply indentation to the entire tree
    indent(root)