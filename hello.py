#!/usr/bin/env python

import textwrap
import sys
from six.moves.BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer


class HelloRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path != '/':
            self.send_error(404, "Object not found")
            return
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        response_text = textwrap.dedent('''\
            <html>
            <head>
                <title>Greetings to the world</title>
            </head>
            <body>
                <h1>Greetings to the world</h1>
                <p>Hello, world!</p>
                <p>Shalom !!!</p>
                <p>Ola !!!</p>
            </body>
            </html>
        ''')
        self.wfile.write(response_text.encode('utf-8'))


		

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

port=sys.argv[1]
print port
portnum = int(port)

server_address = ('', portnum)
httpd = HTTPServer(server_address, HelloRequestHandler)
print "http://hostname:%d" %(portnum)
httpd.serve_forever()
