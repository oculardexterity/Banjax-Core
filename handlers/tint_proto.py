from handlers.base import BaseHandler

import logging
logger = logging.getLogger('boilerplate.' + __name__)


class TintHandler(BaseHandler):
	def get(self):
		self.render("tintForm.html")

	def post(self):
		testArg = self.get_argument("xmlData")
		print("ARG POSTED:", testArg)

		if testArg == 'bad':
			
			self.clear()
			self.set_status(400)
			self.finish({"success": False, "message": "submitted data was literally bad!"})
		self.write({"success": True, "testArg": testArg})

