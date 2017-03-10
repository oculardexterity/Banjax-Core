import os

from settings import ROOT

def banjax_core(self, filename):
	return os.path.join(ROOT, filename)

