import os, sys, shutil
import urllib2
import zipfile
import json
from download import *
from .. import colorama
colorama.init()
from ..colorama import Fore, Back, Style

class remove:
	def __init__(self, packagesList, force):
		self.remove(packagesList,force)

	@staticmethod
	def remove(packagesList,force):
		for (i,packageName) in enumerate(packagesList):
			if force != 1:
				print (Fore.YELLOW + 'REMOVING #'+str(i+1)+ Style.RESET_ALL+' Trying to unbuild package named "'+packageName+'".')
			if os.path.isdir(packageName):
				if force != 1:
					raw_input("Press enter to continue...")
				shutil.rmtree(packageName)
				if force != 1:
					print (Fore.GREEN + 'PACKAGE UNBUILT!' + Style.RESET_ALL)+' Extentions/'+packageName+' directory has been uninstalled.' 
			else:
				if force != 1:
					print (Fore.RED + 'PACKAGE NOT FOUND!' + Style.RESET_ALL)+' Extentions/'+packageName+' directory has not been found.'