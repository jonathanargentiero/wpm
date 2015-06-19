import os, sys, shutil
import urllib2
import zipfile
import json
from download import *
from install import *
from remove import *
from .. import colorama
colorama.init()
from ..colorama import Fore, Back, Style

class list:
	def __init__(self,arguments):
		if len(arguments) == 0:
			self.packagesInstalled = []
			subdirectories = os.listdir(".")
			for subdirectory in subdirectories:
				if os.path.isdir(subdirectory) and subdirectory != 'lib':
					for file in os.listdir(subdirectory):
						if file == 'manifest.json':
							repoUrl = "http://addons.wakanda.org/rest/Addons/?&$filter=%27name%20==%20:1%27&$params=%27[%22"+subdirectory+"%22]%27"
							repoResponse = urllib2.urlopen(repoUrl)
							responseText = repoResponse.read()
							packageJson = json.loads(responseText)
							if packageJson['__COUNT'] == 1:
								self.packagesInstalled.append(subdirectory)
			print (Fore.MAGENTA + 'INSTALLED PACKAGES:' + Style.RESET_ALL)
			if len(self.packagesInstalled) > 0:
				print os.path.dirname(os.path.realpath(__file__))
				for (i,packageName) in enumerate(self.packagesInstalled):
					print '|_'+packageName
			else:
				print 'no packages has been found in this directory.'
		elif arguments[0] == '--all' or arguments[0] == '-a':
			repoUrl = 'http://addons.wakanda.org/rest/Addons/?$orderby="name"'
			repoResponse = urllib2.urlopen(repoUrl)
			responseText = repoResponse.read()
			packagesJson = json.loads(responseText)
			print (Fore.MAGENTA + 'AVAILABLE PACKAGES ('+str(packagesJson['__COUNT'])+'):' + Style.RESET_ALL)
			for (i,packageJson) in enumerate(packagesJson['__ENTITIES']):
				packageVersion = packageJson['version']
				if packageVersion is None:
					packageVersion = 'latest'
				print '|_'+packageJson['name']+'@'+packageVersion

				depRepoUrl = 'http://addons.wakanda.org/rest/Addons('+packageJson['__KEY']+')/dependencies?$expand=dependencies'
				depRepoResponse = urllib2.urlopen(depRepoUrl)
				depResponseText = depRepoResponse.read()
				depPackagesJson = json.loads(depResponseText)
				if depPackagesJson['dependencies']['__COUNT'] > 0:
					for (i,depPackageJson) in enumerate(depPackagesJson['dependencies']['__ENTITIES']):
						print '   |_'+depPackageJson['name']

