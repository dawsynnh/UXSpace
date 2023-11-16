import http.server
import os
from http.server import HTTPServer, CGIHTTPRequestHandler, ThreadingHTTPServer
import ssl
import functools

class httpsserver:
    @staticmethod
    def start_Server_PHP(host, port):
        print("Starting php server from python!")
        cmd = "php -S " + str(host) + ":" + str(port) + " -t index/php/"
        os.system(cmd)

    @staticmethod
    def start_Server(host, port):
        useCGI = input("Would you like to use CGI (y/N) ?")

        if useCGI == "y":
            print("Loading complex Python3 based CGI server...")
            print("Starting service on Port: " + str(port))

            httpd = ThreadingHTTPServer((host, port), CGIHTTPRequestHandler)

            httpd.serve_forever()

        else:
            print("Loading vanilla html Python3 server...")
            print("Starting service on Port: " + str(port))
            context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
            context.load_cert_chain(keyfile="sec/key.pem",
                                    certfile="sec/cert.pem",
                                    password="tg25Ujt67!JgoApwlF8tj!uhF7")

            SimpleHandler = functools.partial(http.server.SimpleHTTPRequestHandler, directory='index/')

            httpd = ThreadingHTTPServer((host, port), SimpleHandler)

            httpd.socket = context.wrap_socket(httpd.socket,
                                               server_side=True)

            httpd.serve_forever()
