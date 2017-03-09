from handlers.base import BaseHandler


from io import StringIO
from lxml import etree

import tornado.gen
from executor import executor

import logging
logger = logging.getLogger('boilerplate.' + __name__)



class TintHandler(BaseHandler):
	
	@tornado.gen.coroutine
	def get(self):
		self.render("tintForm.html")

	@tornado.gen.coroutine
	def post(self):
		xmlData = self.get_argument("xmlData")
		print()
		try:
			yield tornado.gen.sleep(10)
			xmlTree = yield executor.submit(etree.parse, StringIO(xmlData))
			#xmlTree = etree.parse(StringIO(xmlData))
			self.write({"success": True, "testReturnData": xmlData})
		except Exception as e:
			self.clear()
			self.set_status(400)
			self.finish({"success": False, "message": str(e)})
		

