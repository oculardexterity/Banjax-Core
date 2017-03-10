
import tornado
from handlers.foo import FooHandler
from banjax_modules.banjax_tint.tint_proto import TintHandler


url_patterns = [
	# Default static route
	(r'/static/(.*)', tornado.web.StaticFileHandler, dict(path='media')),

    (r"/foo", FooHandler),
    

    # Tint handler and tint static handler
    (r'/tint', TintHandler),
    (r'/banjax_tint/module_assets/(.*)', tornado.web.StaticFileHandler, dict(path='banjax_modules/banjax_tint/module_assets')),
]












"""
for dr in [dr for dr in os.listdir(MODULES_ROOT) if dr.startswith('banjax_')]:
	for f in [f for f in os.listdir(os.path.join(MODULES_ROOT, dr)) \
				 if (f.endswith('.py') and not f.startswith('__'))]:
		print(f)
		spec = importlib.util.spec_from_file_location(f.replace('.py',''), os.path.join(MODULES_ROOT, dr, f))
		print(spec)
		mod = importlib.util.module_from_spec(spec)
		spec.loader.exec_module(mod)
		
		url_patterns += mod.urls()

"""



#from banjax_modules.banjax_tint.tint_proto import TintHandler


