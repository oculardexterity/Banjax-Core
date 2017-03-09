from handlers.foo import FooHandler
from handlers.tint_proto import TintHandler

url_patterns = [
    (r"/tint", TintHandler),
    (r"/foo", FooHandler)
]
