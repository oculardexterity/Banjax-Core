import json
import tornado.web

import logging
logger = logging.getLogger('boilerplate.' + __name__)


class BaseHandler(tornado.web.RequestHandler):


    """A class to collect common handler methods - all other handlers should
    subclass this one.


    RH: thanks for hint. Build in the fucktonne XML validators here.



    RH: Maybe don't need this JSON business below.

    RH: **but** maybe here... probably here! should go a revisionDesc DECORATOR??????
    """


    #SUPPORTED_METHODS = tornado.web.RequestHandler.SUPPORTED_METHODS + ("PATCH",)

    def return_error(self, http_code, message):
        self.clear()
        self.set_status(400)
        self.finish({"success": False, "message": str(message)})

    def load_json(self):
        """Load JSON from the request body and store them in
        self.request.arguments, like Tornado does by default for POSTed form
        parameters.

        If JSON cannot be decoded, raises an HTTPError with status 400.
        """
        try:
            self.request.arguments = json.loads(self.request.body)
        except ValueError:
            msg = "Could not decode JSON: %s" % self.request.body
            logger.debug(msg)
            raise tornado.web.HTTPError(400, msg)

    def get_json_argument(self, name, default=None):
        """Find and return the argument with key 'name' from JSON request data.
        Similar to Tornado's get_argument() method.
        """
        if default is None:
            default = self._ARG_DEFAULT
        if not self.request.arguments:
            self.load_json()
        if name not in self.request.arguments:
            if default is self._ARG_DEFAULT:
                msg = "Missing argument '%s'" % name
                logger.debug(msg)
                raise tornado.web.HTTPError(400, msg)
            logger.debug("Returning default argument %s, as we couldn't find "
                    "'%s' in %s" % (default, name, self.request.arguments))
            return default
        arg = self.request.arguments[name]
        logger.debug("Found '%s': %s in JSON arguments" % (name, arg))
        return arg
