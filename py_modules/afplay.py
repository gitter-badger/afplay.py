#!/usr/bin/env python
from os.path import *
from subopen import *
from osx_only import *
from public import *

@osx_only
@public
def afplay(audiofile="/System/Library/Sounds/Glass.aiff"):
    if not exists(audiofile):
        dir = "/System/Library/Sounds"
        for file in listdir(dir):
            if basename(file).lower()==audiofile.lower() or basename(file).replace(".aiff","").lower()==audiofile.lower():
                audiofile = join(dir,file)
                break
    if not exists(audiofile):
        err = "%s not found" % audiofile
        raise OSError(err)
    args = ["/usr/bin/afplay",audiofile]
    subopen(args)

if __name__=="__main__":
    afplay()
