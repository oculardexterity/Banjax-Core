import inspect
import os

from settings import ROOT
from settings import BASEURL

def banjax_url(self, file_path):
	return os.path.join(BASEURL, file_path)

def module_assets(self, filename):

	calling_file = inspect.getfile(self.__class__)
	print(calling_file)
	if 'banjax_modules' in calling_file:
		module_name = calling_file.split('banjax_modules/')[1].split('/')[0]
		file_path = os.path.join(BASEURL, module_name,'module_assets', filename)

		return  file_path

def static_assets(self, filename):
	return os.path.join(BASEURL, 'static', filename)


