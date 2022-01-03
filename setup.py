#!/usr/bin/env python

import setuptools

# Create or remove html files from the README and TODO
import sys

if sys.argv[1]=='build':
    from os import system
    from docutils.core import publish_file
    print("Creating html files from rst files")
    for s in ['README', 'TODO']:
        publish_file(source_path=s+'.rst',
                     destination_path=s+'.html',
                     writer_name='html')
    # Use bird for the healthchecker special account
    print("Updating systemd service file")
    system("sed 's/^\(User\|Group\)=healthchecker$/\\1=bird/;"+
           "s/^\(After\|Requires\)=network.service/\\1=network.target/' "+
           "contrib/systemd/anycast-healthchecker.service > "+
           "anycast-healthchecker.service")
    # Also create empty sysconfig file, since systemd unit otherwise fails
    print("Create empty sysconfig file")
    f = open("anycast-healthchecker", "w")
    f.write('#RUNASUSER="healthchecker"\n#RUNASGROUP="healthchecker"\n')
    f.close()
elif sys.argv[1]=='clean':
    from os import unlink
    for f in ['README.html', 'TODO.html',
              'anycast-healthchecker.service', 'anycast-healthchecker']:
        try:
            unlink(f)
        except:
            pass


setuptools.setup(
    data_files = [
        ('/usr/lib/systemd/system', ['anycast-healthchecker.service']),
        ('/etc/sysconfig', ['anycast-healthchecker'])
    ],
    setup_requires=['pbr'],
    pbr=True)
