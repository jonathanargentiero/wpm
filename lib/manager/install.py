import os, sys, shutil
import urllib2
import zipfile
import json
from download import *
from .. import colorama
colorama.init()
from ..colorama import Fore, Back, Style

class install:
	def __init__(self, packagesList):
		self.install(packagesList)

	@staticmethod
	def install(packagesList):
		for (i,packageName) in enumerate(packagesList):
			print (Fore.MAGENTA + 'INSTALLING #'+str(i+1)+ Style.RESET_ALL+' Trying to retrieve package named "'+packageName+'".') 
			repoUrl = "http://addons.wakanda.org/rest/Addons/?&$filter=%27name%20==%20:1%27&$params=%27[%22"+packageName+"%22]%27"
			repoResponse = urllib2.urlopen(repoUrl)
			responseText = repoResponse.read()
			packageJson = json.loads(responseText)
			if packageJson['__COUNT'] == 1:
				packageUrl = packageJson['__ENTITIES'][0]['html_url'].replace('/tree/','/archive/')
				packageVersion = packageJson['__ENTITIES'][0]['version']
				if packageVersion is None:
					packageVersion = "latest"
				packageUrlSplitted = packageUrl.split('/')
				packageUrl += '.zip'			
				print (Fore.GREEN + '200: FOUND!' + Style.RESET_ALL)+' '+packageUrl
				try:
					packageName = packageJson['__ENTITIES'][0]['name']
					if os.path.isdir(packageName):
						print (Fore.RED + 'DIRECTORY NOT EMPTY!' + Style.RESET_ALL)+' Extentions/'+packageName+' directory is not empty. Aborting.' 
					else:
						#raw_input("Press enter to continue...")
						download(packageUrl,packageName+'.zip')
						print (Fore.BLUE + 'EXTRACTING!' + Style.RESET_ALL)
						with zipfile.ZipFile(packageName+'.zip', 'r') as z:
							z.extractall()

						tempFolderName = packageName+'-'+packageUrlSplitted[len(packageUrlSplitted)-1]
						os.rename(tempFolderName,packageName)
						#print (Fore.BLUE + 'REMOVING .ZIP!' + Style.RESET_ALL)+' '+packageName+'.zip' 
						os.remove(packageName+'.zip')
						print (Fore.GREEN + 'PACKAGE INSTALLED!' + Style.RESET_ALL)+' '+packageName+'@'+packageVersion
				except (IOError):
					return 1


			elif packageJson['__COUNT'] == 0:
				print (Fore.RED + '404: NOT FOUND!' + Style.RESET_ALL)+' package was not found.'
			else:
				print (Fore.YELLOW + '500: CONFLICT!' + Style.RESET_ALL)+'  multiple packages under the same name'