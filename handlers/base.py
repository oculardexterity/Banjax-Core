'''
Break this up into separate folders!
Especially this `base` needs to be hidden away in a lib dir.
Reserving the handlers dir for actual handlers.

'''

import inspect
import json
import os
import sys
import tornado.web
from tornado import template

import logging
logger = logging.getLogger('boilerplate.' + __name__)


from settings import ROOT



class modLoader(template.Loader):
    '''
        A subclassed template.Loader to point back to Banjax-Core template 
        folder for default templates
    '''

    def resolve_path(self, name, parent_path=None):
      
        if 'Banjax/' in name:
            name = os.path.join(ROOT, 'templates', name.replace('Banjax/', ''))

        if parent_path and not parent_path.startswith("<") and \
            not parent_path.startswith("/") and \
                not name.startswith("/"):
            current_path = os.path.join(self.root, parent_path)
            file_dir = os.path.dirname(os.path.abspath(current_path))
            relative_path = os.path.abspath(os.path.join(file_dir, name))
            if relative_path.startswith(self.root):
                name = relative_path[len(self.root) + 1:]

        return name





class BaseHandler(tornado.web.RequestHandler):


    """A class to collect common handler methods - all other handlers should
    subclass this one.


    RH: thanks for hint. Build in the fucktonne XML validators here.



    RH: Maybe don't need this JSON business below.

    RH: **but** maybe here... probably here! should go a revisionDesc DECORATOR??????
    """



    def get_template_path(self):
        '''
            Overriding get_template_path function.
            
            Inspects the file of the class that is calling the template render.
            Assumes templates are in dir called `module_templates` inside the
            module dir. May need to modify module_name variable below to get
            correct dir (if it doesn't work)

        '''
        
        calling_file = inspect.getfile(self.__class__)


        if 'banjax_modules' in calling_file:
            module_name = calling_file.split('banjax_modules/')[1].split('/')[0]
            file_path = os.path.join(ROOT, 'banjax_modules', module_name,'module_templates')
            return file_path
        return os.path.join(ROOT, 'templates')



    def render_string(self, template_name, **kwargs):
        """Generate the given template with the given arguments.

        We return the generated byte string (in utf8). To generate and
        write a template as a response, use render() above.
        """
        # If no template_path is specified, use the path of the calling file
        template_path = self.get_template_path()

        '''

        # THIS is crossed out for some reason; I think because
        # building by convention allows two options to be essentially
        # hard-coded: either pointing to core templates or module templates


        if not template_path:
            frame = sys._getframe(0)
            web_file = frame.f_code.co_filename
            while frame.f_code.co_filename == web_file:
                frame = frame.f_back
            template_path = os.path.dirname(frame.f_code.co_filename)
        '''
        with tornado.web.RequestHandler._template_loader_lock:
            if template_path not in tornado.web.RequestHandler._template_loaders:
                
                loader = self.create_template_loader(template_path)
                tornado.web.RequestHandler._template_loaders[template_path] = loader
            else:
                loader = tornado.web.RequestHandler._template_loaders[template_path]

        t = loader.load(template_name)
        namespace = self.get_template_namespace()
        namespace.update(kwargs)
        return t.generate(**namespace)


    def create_template_loader(self, template_path):
        """Returns a new template loader for the given path.

        May be overridden by subclasses.  By default returns a
        directory-based loader on the given path, using the
        ``autoescape`` and ``template_whitespace`` application
        settings.  If a ``template_loader`` application setting is
        supplied, uses that instead.
        """
        settings = self.application.settings
        

        '''
        # Don't use the default template path under any circs.


        if "template_loader" in settings and not is_module:
            return settings["template_loader"]
        '''
        

        kwargs = {}
        if "autoescape" in settings:
            # autoescape=None means "no escaping", so we have to be sure
            # to only pass this kwarg if the user asked for it.
            kwargs["autoescape"] = settings["autoescape"]
        if "template_whitespace" in settings:
            kwargs["whitespace"] = settings["template_whitespace"]

        # Return the modified template loader.
        return modLoader(template_path, **kwargs)
        










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
