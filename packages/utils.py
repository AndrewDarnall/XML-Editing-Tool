""" Contains Utility functions for the project """

from os import listdir
import xml.etree.ElementTree as ET

from packages.xml_editor import tree_visit, prettify_xml, load_xml_file, replacements




def load_dir(input_dir: str) -> None:
    """
        load_dir: Sequentially edits all .xml files present in the directory
        @param input_dir: commandline argument of input target directory where all .xml files are
    """


    for file in listdir(input_dir):
        try:
            # Load the xml file and parse it into a tree structure, saving the root and the structure
            root, tree = load_xml_file(file)
        except ET.ParserError as e:
            print(f" -- Caught exception:\t{e}")
            continue
        # Recursively visit the tree whilst searching for the target node and make the required midifications
        tree_visit(root, replacements)
        # Pretty-format the xml file to respect indentation (not required but usually appreciated)
        prettify_xml(root)
        # Save the performed changes into the chosen file (the same file in this case)
        tree.write(file, encoding="utf-8", xml_declaration=True)
