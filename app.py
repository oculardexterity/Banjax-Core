#!/usr/bin/env python
import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.options import options

from settings import settings
import ui_methods
from urls import url_patterns




class TornadoBoilerplate(tornado.web.Application):
    def __init__(self):
        tornado.web.Application.__init__(self, url_patterns, ui_methods=ui_methods, **settings)


def main():
    
    run_on_cpu_cores = int(settings['autoreload'])
    print("Tornado server (re)started\nCPU count:", tornado.process.cpu_count(), 
    	"\nRunning on", tornado.process.cpu_count() if not run_on_cpu_cores else run_on_cpu_cores, 
    	'core(s)', '[autoreload enabled]' if run_on_cpu_cores else '[autoreload disabled]',
    	 '\n------------------------------------------')


    app = TornadoBoilerplate()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.bind(options.port)
    http_server.start(run_on_cpu_cores)  # autodetect number of cores and fork a process for each
    tornado.ioloop.IOLoop.current().start()
    

if __name__ == "__main__":
    main()
