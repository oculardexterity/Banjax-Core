#!/usr/bin/env python
import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.options import options

from settings import settings
from urls import url_patterns




class TornadoBoilerplate(tornado.web.Application):
    def __init__(self):
        tornado.web.Application.__init__(self, url_patterns, **settings)


def main():
    app = TornadoBoilerplate()
    print("Tornado server started\nCPU count:", tornado.process.cpu_count())
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.bind(options.port)
    http_server.start(0)  # autodetect number of cores and fork a process for each
    tornado.ioloop.IOLoop.current().start()
    

if __name__ == "__main__":
    main()
