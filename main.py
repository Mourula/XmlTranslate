#!/usr/bin/env python
# -*- coding: latin-1 -*-

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

        print('Translating {} items:'.format(len(root)))
        for amount in range(len(root)):
            source = root[amount][1].text
            if source is None:
                continue
            dest = ts.google(source, from_language='en', to_language='fi')
            if dest is not None:
                root[amount][2].text = dest
                root[amount][3].text = "1"
            print(".", end='', flush=True)

        tree.write("output.xml", encoding='utf-8')

    except Exception as exep:
        print(" ")
        print("ERROR: Cannot read/write the XML file")
        print(exep)
        return

    print(" All done. Check output.xml")


if __name__ == '__main__':
    main(sys.argv[1:])
