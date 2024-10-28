""" Driver code for the XML-Editor-Tool  """

# STL imports
from sys import argv, exit

# Third party imports

# Local imports
from packages.utils import load_dir
from packages.xml_editor import expand_path

if len(argv) != 2:
    print(f"usage:\t{argv[1]}\t<INPUT-DIR-PATH")
    exit(-1)


# Entrypoint
if __name__ == "__main__":
    load_dir(expand_path(argv[1]))
    print(f" [*] {argv[1]} has been edited  [*] ")
