#!/usr/bin/env python3

"""Main."""

import sys
import os
from cpu import *
from ast import literal_eval

# path = "ls8/examples/print8.ls8" # to print 8
# path = "ls8/examples/mult.ls8" # to do + MUL command
# path = "ls8/examples/stack.ls8"
path = "ls8/examples/call.ls8"

cpu = CPU()
cpu.load(path)
cpu.run()