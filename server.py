from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from cowpy import cow
import json


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        parsed_qs = parse_qs(parsed_path.query)

        if parsed_path.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('test.html') as rf:
                greeting = bytes(rf.read(), 'utf-8')
            self.wfile.write(greeting)
            return

        if parsed_path.path == '/cow':
            if 'msg' in parsed_qs:
                self.send_response(200)
                self.send_header('Content-type', 'text')
                self.end_headers()
                bessie = cow.Stegosaurus()
                msg = bessie.milk((parsed_qs['msg'][0]))
                self.wfile.write(bytes(msg, 'utf-8'))
                return

            self.send_response(400)
            self.end_headers()
            return

        self.send_response(404)
        self.end_headers()

    def do_POST(self):
        parsed_path = urlparse(self.path)
        parsed_qs = parse_qs(parsed_path.query)

        if parsed_path.path == '/':
            self.send_response(400)
            self.end_headers()
            return

        if parsed_path.path == '/cow':
            if 'msg' in parsed_qs:
                self.send_response(201)
                self.send_header('Content-type', 'text')
                self.end_headers()
                bessie = cow.Stegosaurus()
                msg = bessie.milk((parsed_qs['msg'][0]))
                content = {}
                content['msg'] = msg
                print(json.dumps(content))
                return

            self.send_response(400)
            self.end_headers()
            return

        self.send_response(404)
        self.end_headers()

    def do_HEAD(self):
        parsed_path = urlparse(self.path)
        parsed_qs = parse_qs(parsed_path.query)

        if parsed_path.path == '/':
            self.send_response(400)
            self.end_headers()
            return

        if parsed_path.path == '/cow':
            if 'msg' in parsed_qs:
                self.send_response(405)
                self.end_headers()
                return

        self.send_response(404)
        self.end_headers()

    def do_PUT(self):
        parsed_path = urlparse(self.path)
        parsed_qs = parse_qs(parsed_path.query)

        if parsed_path.path == '/':
            self.send_response(400)
            self.end_headers()
            return

        if parsed_path.path == '/cow':
            if 'msg' in parsed_qs:
                self.send_response(405)
                self.end_headers()
                return

        self.send_response(404)
        self.end_headers()


def create_server():
    return HTTPServer(
        ('127.0.0.1', 5000),
        SimpleHTTPRequestHandler
    )


def run_forever():
    server = create_server()

    try:
        print(f'Starting server on 127.0.0.1:5000')
        server.serve_forever()
    except KeyboardInterrupt as err:
        print('Thanks for running the server. Shutting down')
        print(err)
        server.server_close()
        server.shutdown()


if __name__ == "__main__":
    run_forever()
