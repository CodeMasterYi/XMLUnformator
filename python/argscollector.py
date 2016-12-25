#!/usr/bin python

import argparse

def getArgs():

    parser = argparse.ArgumentParser(description='Unformat xml file.', fromfile_prefix_chars ='@')

    parser.add_argument('-F', dest='files', metavar='File', type=str, nargs='*')
    parser.add_argument('-s', dest='src', nargs='?', type=str, const='.', default='.')
    parser.add_argument('-d', dest='dst', nargs='?', type=str, const='.', default='.')
    parser.add_argument('-S', dest='salt', nargs='?', type=str, const='Hello, Python!', default='Hello, Python!')

    args = parser.parse_args()

    return args

args = getArgs()
