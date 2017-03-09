import tornado.concurrent

executor = tornado.concurrent.futures.ThreadPoolExecutor(8)