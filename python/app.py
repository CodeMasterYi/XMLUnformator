#!/usr/bin python

from argscollector import args
from xmlstrip import XMLStrip
import os, sys
from hashlib import md5
import json

print args

files = sorted(args.files)

### choose which file to strip
index = 0
for option in files:
    print '===> %-2d' % index, ':', option
    index += 1
print '===> %-2d' % index, ':', 'All above'

choice = input('Choose a number: ')
choices = []
if isinstance(choice, int):
    if 0 <= choice < index:
        choices.append(files[choice])
    elif choice == index:
        choices = files

if len(choices) == 0:
    print 'wrong input or out of range!'
    exit(-1)

### strip what you choose
for filename in choices:
    print
    filepath = filename + '.xml'
    filepath = os.path.join(args.src, filepath)
    print 'parsing', filepath
    xs = XMLStrip(filepath)

    dst = dict()
    dst['data'] = xs.strip()

    ### make a md5 digest
    m = md5()
    m.update(args.salt)
    m.update(dst['data'])
    dst['sign'] = m.hexdigest().lower()

    print m.hexdigest()

    ### write into output file
    dstfilepath = os.path.join(args.dst, filename+'.json')
    print 'writing', dstfilepath
    with open(dstfilepath, 'w') as f:
        f.write(json.dumps(dst))
    print 'success'
