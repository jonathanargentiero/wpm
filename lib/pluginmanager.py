import os, sys, shutil
import urllib2
import zipfile
import json
import colorama
colorama.init()
from manager.install import *
from manager.remove import *
from manager.update import *
from manager.purge import *

class pluginmanager:
	def __init__(self, arguments):
		'''Download a file, you must catch errors yourself'''
		'''Just a class to download files using urllib'''
		self.arguments = arguments

		# script
		if len(self.arguments) < 2:
			print (Fore.RED + 'ERROR: INVALID COMMAND!' + Style.RESET_ALL)+' try "wpm commands".'
			return 1

		if len(self.arguments) < 3:
			if self.arguments[1] == 'install' or self.arguments[1] == 'remove' :
				print (Fore.YELLOW + 'YELLOW: NO PACKAGES SPECIFIED!' + Style.RESET_ALL) +' add at least one package name.'
				return None

		self.packages = []

		for (i,argv) in enumerate(arguments):
			if i > 1:
				self.packages.append(argv)

		self.command = arguments[1]
		if self.command == 'install':
			install(self.packages)
		elif self.command == 'remove': 
			remove(self.packages,None)
		elif self.command == 'update':
			update(self.packages)
		elif self.command == 'purge':
			purge()
		else:
			print (Fore.RED + 'COMMAND NOT IMPLEMENTED YET!' + Style.RESET_ALL)
			return None

	#@staticmethod

