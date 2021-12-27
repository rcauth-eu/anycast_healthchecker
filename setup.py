#!/usr/bin/env python

import setuptools

# Create or remove html files from the README and TODO
import sys

if sys.argv[1]=='build':
    print("Creating html files from rst files")
    from docutils.core import publish_file
    for s in ['README', 'TODO']:
        publish_file(source_path=s+'.rst',
                     destination_path=s+'.html',
                     writer_name='html')
elif sys.argv[1]=='clean':
    from os import unlink
    for f in ['README.html', 'TODO.html']:
        try:
            unlink(f)
        except:
            pass


setuptools.setup(
    setup_requires=['pbr'],
    pbr=True)
