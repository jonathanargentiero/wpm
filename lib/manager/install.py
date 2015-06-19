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
	def scaffoldPackage(packageName,packageUrl):
		packageUrlSplitted = packageUrl.split('/')
		tempFolderName = packageName+'-'+packageUrlSplitted[len(packageUrlSplitted)-1]
		shutil.move(tempFolderName,packageName)
		os.remove(packageName+'.zip')

	def getPackageJsonByName(self,packageName):
		repoUrl = "http://addons.wakanda.org/rest/Addons/?&$filter=%27name%20==%20:1%27&$params=%27[%22"+packageName+"%22]%27"
		repoResponse = urllib2.urlopen(repoUrl)
		responseText = repoResponse.read()
		return json.loads(responseText)

	def getPackageZipUrlByGitUrl(self,packageGitUrl):
		return packageGitUrl.replace('/tree/','/archive/') + '.zip'	

	def getDependencyJsonByKey(self,depKey):
		depRepoUrl = 'http://addons.wakanda.org/rest/Addons('+depKey+')/dependencies?$expand=dependencies'
		depRepoResponse = urllib2.urlopen(depRepoUrl)
		depResponseText = depRepoResponse.read()
		return json.loads(depResponseText)

	def install(self,packagesList):
		for (i,packageName) in enumerate(packagesList):
			print (Fore.MAGENTA + 'INSTALLING #'+str(i+1)+ Style.RESET_ALL+' Trying to retrieve package named "'+packageName+'".') 
			packageJson = self.getPackageJsonByName(packageName)
			if packageJson['__COUNT'] == 1:
				packageGitUrl = packageJson['__ENTITIES'][0]['html_url']
				packageUrl = self.getPackageZipUrlByGitUrl(packageGitUrl)
				print (Fore.GREEN + '200: FOUND!' + Style.RESET_ALL)+' '+packageUrl
				try:
					# package details
					packageName = packageJson['__ENTITIES'][0]['name']
					packageVersion = packageJson['__ENTITIES'][0]['version']
					if packageVersion is None:
						packageVersion = "latest"
					#if os.path.isdir(packageName):
					#	print (Fore.RED + 'DIRECTORY NOT EMPTY!' + Style.RESET_ALL)+' Extentions/'+packageName+' directory is not empty. Aborting.' 
					
					download(packageUrl,packageName+'.zip')
					#print (Fore.BLUE + 'EXTRACTING!' + Style.RESET_ALL)
					with zipfile.ZipFile(packageName+'.zip', 'r') as z:
						z.extractall()

					# os operations
					self.scaffoldPackage(packageName,packageGitUrl)
					print packageName+'@'+packageVersion

					# dependencies
					depPackagesJson = self.getDependencyJsonByKey(packageJson['__ENTITIES'][0]['__KEY'])
					if depPackagesJson['dependencies']['__COUNT'] > 0:
						for (i,depPackageJson) in enumerate(depPackagesJson['dependencies']['__ENTITIES']):
							depJson = self.getPackageJsonByName(depPackageJson['name'])
							depGitUrl = depJson['__ENTITIES'][0]['html_url']
							depUrl = self.getPackageZipUrlByGitUrl(depGitUrl)
							depName = depJson['__ENTITIES'][0]['name']
							depVersion = depJson['__ENTITIES'][0]['version']
							if depVersion is None:
								depVersion = "latest"

							download(depUrl,depName+'.zip')
							#print (Fore.BLUE + 'EXTRACTING!' + Style.RESET_ALL)
							with zipfile.ZipFile(depName+'.zip', 'r') as z:
								z.extractall()

							self.scaffoldPackage(depName,depGitUrl)
							print '   |_'+depName+'@'+depVersion

					print (Fore.GREEN + 'PACKAGE INSTALLED!' + Style.RESET_ALL)
				except (IOError):
					return 1


			elif packageJson['__COUNT'] == 0:
				print (Fore.RED + '404: NOT FOUND!' + Style.RESET_ALL)+' package was not found.'
			else:
				print (Fore.YELLOW + '500: CONFLICT!' + Style.RESET_ALL)+'  multiple packages under the same name'