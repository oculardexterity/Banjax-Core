from handlers.base import BaseHandler

import logging
logger = logging.getLogger('boilerplate.' + __name__)


class TintHandler(BaseHandler):
    def get(self):
        self.render("base.html")

    def post(self):
    	testArg = self.get_argument("test")
    	self.write({"success": True, "testArg": testArg})

