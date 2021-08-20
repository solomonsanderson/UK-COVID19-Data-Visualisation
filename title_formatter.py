'''
This script takes the parameters used to make an api request to make them 
appropriate for ax titles.
'''

import re


def title_formatter(column):
    title_chars = [char for char in column]
    title_chars[0] = title_chars[0].upper()
    title_cap = ''.join(title_chars)
    res_list = []
    res_list = re.findall('[A-Z][^A-Z]*', title_cap)
    title = ' '.join(res_list)    
    return title
