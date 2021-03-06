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
from manager.list import *

class pluginmanager:
	def __init__(self, arguments):

		self.__version__ = "0.3.2"
		self.__doc__ = (Fore.MAGENTA + 'Wakanda Package Manager' + Style.RESET_ALL)+'\n'
		self.__doc__ += (Fore.GREEN + 'version '+self.__version__ + Style.RESET_ALL)+'\n'
		self.__doc__ += 'A package management tool\nRun "python wpm --help" for a list of commands.'

		self.__help__ = (Fore.RED + 'All the commands should be run in the directory where you want to manage packages!' + Style.RESET_ALL)+'\n'
		self.__help__ += 'Usage:\n'
		self.__help__ += 'python wpm [options] [arguments]\n\n'
		self.__help__ += 'Options:\n'
		self.__help__ += '   -h, --help        	  	print this command list\n'
		self.__help__ += '   -v, --version        	print version\n'
		self.__help__ += '   list     			list all packages installed in the directory\n'	
		self.__help__ += '   list --all        	        list all packages available on the addons repository\n'	
		self.__help__ += '   install [package,..]        	installs one or more packages\n'
		self.__help__ += '   remove [package,..]        	removes one or more packages\n'
		self.__help__ += '   update [package,..]        	updates one or more packages\n'
		self.__help__ += '   update        	        updates all packages\n'
		self.__help__ += '   update --self        	updates the WPM\n'
		self.__help__ += '   purge        	        purge all packages\n'	
		self.__help__ += '\n'+(Fore.YELLOW + 'WARNING: WPM is experimental. Version checks are lazy and manual modifications on extensions/widgets are ignored.' + Style.RESET_ALL)+'\n'



		self.arguments = arguments

		# script
		if len(self.arguments) < 2:
			print self.__doc__
			return None

		if len(self.arguments) < 3:
			if self.arguments[1] == 'install' or self.arguments[1] == 'remove' :
				print (Fore.YELLOW + 'YELLOW: NO PACKAGES SPECIFIED!' + Style.RESET_ALL) +' add at least one package name.'
				return None

		self.agvs = []

		for (i,argv) in enumerate(arguments):
			if i > 1:
				self.agvs.append(argv)

		self.command = arguments[1]
		if self.command == 'install':
			install(self.agvs)
		elif self.command == 'remove': 
			remove(self.agvs,None)
		elif self.command == 'update':
			update(self.agvs)
		elif self.command == 'purge':
			print (Fore.YELLOW + 'WARNING!' + Style.RESET_ALL)+' this will remove all the installed packages in this folder! Continue? [y/n]'
			choice = raw_input().lower()
			if choice in ['yes','y', 'ye', '']:
			   purge()
			elif choice in ['no','n']:
			   return None
			else:
			   sys.stdout.write((Fore.RED + 'UNVALID!' + Style.RESET_ALL)+" please respond with 'yes' or 'no'\n")
			   return None

		elif self.command == 'list':
			list(self.agvs)
		elif self.command == '-h' or self.command == '--help':
			print self.__help__
		elif self.command == '-v' or self.command == '--version':
			print 'v'+self.__version__
		else:
			print (Fore.RED + 'COMMAND NOT IMPLEMENTED YET!' + Style.RESET_ALL)
			return None

	#@staticmethod

