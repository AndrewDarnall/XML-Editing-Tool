from packages.xml_editor import tree_visit, prettify_xml, load_xml_file, replacements
import os

def load_dir(input_dir):
    print(" - Input Directory:\t{}".format(input_dir))
    for file in os.listdir(input_dir):
            print("File:\t{}".format(file))
            # Load the xml file and parse it into a tree structure, saving the root and the structure
            root, tree = load_xml_file(file)
            # Recursively visit the tree whilst searching for the target node and make the required midifications
            tree_visit(root, replacements)
            # Pretty-format the xml file to respect indentation (not required but usually appreciated)
            prettify_xml(root)
            # Save the performed changes into the chosen file (the same file in this case)
            tree.write(file, encoding="utf-8", xml_declaration=True)