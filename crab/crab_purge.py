#!/usr/bin/env python

import os, sys

for p in sys.argv[1:]:
    os.system('crab purge -d ' + p)

