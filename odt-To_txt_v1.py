#!/usr/bin/env python3
"""
ODT to TXT Converter
====================

Converts an ODT file to a TXT file.
"""

import os
from odf.opendocument import load
from odf.text import P, H
from odf import teletype


def convert_odt_to_txt(odt_file_path, txt_file_path):
    """
    Converts the content of an ODT file to a TXT file.

    :param odt_file_path: Path to the input ODT file
    :param txt_file_path: Path to the output TXT file
    """
    # Check if ODT file exists
    if not os.path.isfile(odt_file_path):
        raise FileNotFoundError(f"The file {odt_file_path} does not exist.")

    # Load the ODT file
    doc = load(odt_file_path)

    # Extract text from the ODT file
    with open(txt_file_path, 'w', encoding='utf-8') as txt_file:
        # Iterate through all paragraph elements
        for element in doc.getElementsByType(P):
            txt_file.write(teletype.text_to_string(element) + '\n')
        # Iterate through all heading elements
        for element in doc.getElementsByType(H):
            txt_file.write(teletype.text_to_string(element) + '\n')


if __name__ == "__main__":
    # Define the path to the ODT file and the output TXT file
    odt_file_path = '/home/jasvir/Documents/Princess Rosa/ODT/Collection of Poems_1_1_1.odt'
    txt_file_path = '/home/jasvir/Documents/Princess Rosa/ODT/Collection_of_Poems_1_1_1.txt'

    try:
        convert_odt_to_txt(odt_file_path, txt_file_path)
        print(f"Successfully converted {odt_file_path} to {txt_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
