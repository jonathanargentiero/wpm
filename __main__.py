#!/usr/bin/env python
# file app/__main__.py

# libraries
import os, sys
from lib.pluginmanager import *

__all__ = ("main")

def main():
	try:
		pluginmanager(sys.argv)
	except (IOError):
		return 1
	return 0

if __name__ == '__main__':
	if main():
		print("Oh noes errors happenned :(")

	#raw_input("Press enter to continue...")
