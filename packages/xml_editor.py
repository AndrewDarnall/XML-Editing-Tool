""" Contains the main functions for the XML-Editor tool """

from os.path import abspath
from sys import exit as EXIT_FAILURE
from typing import Tuple
import xml.etree.ElementTree as ET


from packages.string_definitions import ADD_STRING_1, ADD_STRING_2, EDIT_STRING


# Dictionary of target nodes and XML replacements
replacements = {
    "addition": ("ListOfReferenceCoded", (ADD_STRING_1, ADD_STRING_2)),
    "modification": ("BuyerParty", EDIT_STRING),
}


def expand_path(rel_path: str) -> str:
    """
    expand_path: Expands the input PATH to an Absolute PATH
    @param rel_path: relative PATH
    """
    return abspath(rel_path)


def load_xml_file(target_file: str) -> Tuple[ET.Element, ET.ElementTree]:
    """
    load_xml_file: Loads the XML file and parses it into a Tree structure
    @param target_file: the input relative path of the target-directory
    """
    abs_path = expand_path(target_file)
    tree = ET.parse(abs_path)
    root = tree.getroot()
    return root, tree


def tree_visit(node: ET.Element, replacements: dict) -> None:
    """
    tree_visit: Performs a recursive visit of the XML element tree, searching for the target nodes
                on which to perform the appropriate changes

    @param node: the node to be visited
    @param replacements: the replacement dictionary
    """

    for child in node:

        if child.tag == replacements["addition"][0]:

            try:
                # Add the two nodes separaterly due to how XML requires
                # the structure of the portion of code to be added
                new_node_1 = ET.fromstring(replacements["addition"][1][0])
                new_node_2 = ET.fromstring(replacements["addition"][1][1])
            except ET.ParseError:
                print(" --> Failed to parse the string into xml node: addition")
                EXIT_FAILURE(-1)

            child.append(new_node_1)
            child.append(new_node_2)

        if child.tag == replacements["modification"][0]:

            child.clear()

            try:
                new_node = ET.fromstring(replacements["modification"][1])
            except ET.ParseError:
                print(" --> Failed to parse the string into xml node: modification")
                EXIT_FAILURE(-1)

            child.append(new_node)

        tree_visit(child, replacements)


def prettify_xml(root: ET.Element) -> None:
    """
    prettify_xml: Prettify the XML file (fix indentation and spacing)
    @param root: root of the XML file
    """

    def indent(elem, level=0) -> None:
        """
        indent: Inner function that performs the actual recursive indentation
        @param elem: Visited node
        @param level: current tree level (recusion depth)
        """
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
