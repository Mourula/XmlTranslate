#!/usr/bin/env python

import sys
import xml.etree.ElementTree as ET
import translators as ts


def main(args):

    if len(args) < 1:
        print("ERROR: Give XML file as an argument.")
        return

    filename = args[0]

    try:
        tree = ET.parse(filename)

        root = tree.getroot()

        for amount in range(len(root)):
            source = root[amount][5].text
            dest = ts.google(source, from_language='en', to_language='fi')
            if dest is not None:
                title = ET.Element('description_fi')
                title.text = dest
                root[amount].append(title)

        tree.write("sample_test.xml")

    except Exception as exep:
        print("ERROR: Cannot read the XML file")
        print(exep)
        return


if __name__ == '__main__':
    main(sys.argv[1:])
