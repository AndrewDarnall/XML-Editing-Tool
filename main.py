# Driver code for the script

import sys
from packages.utils import load_dir
from packages.xml_editor import expand_path

if len(sys.argv) != 2:
    print("usage:\t{}\t<INPUT-DIR-PATH".format(sys.argv[0]))
    sys.exit(-1)


# Entrypoint
if __name__ == "__main__":
    load_dir(expand_path(sys.argv[1]))
    print(" [*] {} has been edited  [*] ".format(sys.argv[1]))
