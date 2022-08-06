from collections import defaultdict
import pandas as pd
import xml.etree.ElementTree as ET
from typing import Union


def recursive_xml_flattening(xml_element: Union[ET.ElementTree, ET.Element],
                             flattened_dict:
                             defaultdict, tag ='',
                             name_separator='.'):
    if isinstance(xml_element, ET.ElementTree):
        xml_element = xml_element.getroot()
    if tag != '':
        tag += name_separator
    for element in xml_element:
        if len(element) == 0:
            flattened_dict[tag+element.tag].append(element.text)
            continue
        recursive_xml_flattening(element, flattened_dict, tag + element.tag)

def xml2df(path_to_file: str)-> pd.DataFrame:
    tree = ET.parse(path_to_file)
    flattened_dict = defaultdict(list)
    recursive_xml_flattening(tree, flattened_dict)
    return  pd.DataFrame.from_dict(flattened_dict, orient='index').T
