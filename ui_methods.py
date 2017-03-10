import inspect
import os

from settings import ROOT

def banjax_core(self, filename):
	return os.path.join(ROOT, filename)

def module_assets(self, filename):
	print(filename)
	calling_file = inspect.getfile(self.__class__)
	if 'banjax_modules' in calling_file:
		module_name = calling_file.split('banjax_modules/')[1].split('/')[0]
		file_path = os.path.join(module_name,'module_assets', filename)
		return file_path

def static_assets(self, filename):

	print('static requests')
	return os.path.join('static', filename)