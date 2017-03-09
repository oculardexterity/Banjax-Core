from handlers.base import BaseHandler

import logging
logger = logging.getLogger('boilerplate.' + __name__)


class TintHandler(BaseHandler):
    def get(self):
        self.render("tintForm.html")

    def post(self):
    	testArg = self.get_argument("xmlData")
    	print("ARG POSTED:", testArg)
    	self.write({"success": True, "testArg": testArg})

