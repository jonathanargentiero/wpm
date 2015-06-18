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

class update:
	def __init__(self, packagesList):
		if len(packagesList) == 0:
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
								print (Fore.MAGENTA + 'UPDATING' + Style.RESET_ALL+' package named "'+subdirectory+'".') 
								remove([subdirectory],1)
								install([subdirectory])
		elif packagesList[0] == '--self':
			print '@todo'
		else:
			remove(packagesList,1)
			install(packagesList)