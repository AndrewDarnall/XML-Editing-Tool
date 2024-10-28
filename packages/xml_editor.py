import xml.etree.ElementTree as ET

from packages.string_definitions import ADD_STRING_1, ADD_STRING_2, EDIT_STRING

from sys import argv
from os.path import abspath, exit
from typing import Tuple


# Dictionary of target nodes and XML replacements
replacements = {
    "addition": ("ListOfReferenceCoded", (ADD_STRING_1, ADD_STRING_2)),
    "modification": ("BuyerParty", EDIT_STRING),
}


"""
    expand_path: Expands the input PATH to an Absolute PATH
    @param rel_path: relative PATH

"""


def expand_path(rel_path: str) -> str:
    return abspath(rel_path)


"""
    load_xml_file: Loads the XML file and parses it into a Tree structure
    @param target_file: the input relative path of the target-directory
"""


def load_xml_file(target_file: str) -> Tuple[ET.Element, ET.ElementTree]:
    abs_path = expand_path(target_file)
    tree = ET.parse(abs_path)
    root = tree.getroot()
    return root, tree


"""
    tree_visit: Performs a recursive visit of the XML element tree, searching for the target nodes
                on which to perform the appropriate changes

    @param node: the node to be visited
    @param replacements: the replacement dictionary
"""


def tree_visit(node: ET.Element, replacements: dict) -> None:

    for child in node:

        if child.tag == replacements["addition"][0]:

            try:
                # Add the two nodes separaterly due to how XML requires the structure of the portion of code to be added
                new_node_1 = ET.fromstring(replacements["addition"][1][0])
                new_node_2 = ET.fromstring(replacements["addition"][1][1])
            except Exception as e:
                print(" --> Failed to parse the string into xml node: addition")
                print(e)
                exit(-1)

            child.append(new_node_1)
            child.append(new_node_2)

        if child.tag == replacements["modification"][0]:

            child.clear()

            try:
                new_node = ET.fromstring(replacements["modification"][1])
            except Exception as e:
                print(" --> Failed to parse the string into xml node: modification")
                exit(-1)

            child.append(new_node)

        tree_visit(child, replacements)


"""
    prettify_xml: Prettify the XML file (fix indentation and spacing)
    @param root: root of the XML file
"""


def prettify_xml(root: ET.Element) -> None:
    """
    indent: Inner function that performs the actual recursive indentation
    @param elem: Visited node
    @param level: current tree level (recusion depth)
    """

    def indent(elem, level=0) -> None:

        # Indentation accumulator
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

    indent(root)
