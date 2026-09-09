from http.server import HTTPServer, BaseHTTPRequestHandler
import datetime
import json


LOG = []


class HoneyHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        entry = {
            "time": str(datetime.datetime.now()),
            "ip": self.client_address[0],
            "path": self.path,
            "agent": self.headers.get("User-Agent", "?")
        }

        LOG.append(entry)

        print("\n===== HONEYPOT VISIT DETECTED =====")
        print(json.dumps(entry, indent=2))

        self.send_response(200)
        self.end_headers()

        self.wfile.write(
            b"Thanks for visiting! This is a cybersecurity awareness simulation."
        )

    def log_message(self, *args):
        # Suppress default server logs
        pass


print("======================================")
print("       HONEYPOT LINK TRACKER")
print("======================================")
print("Honeypot running on:")
print("http://127.0.0.1:8080")
print("\nOpen the URL in your browser to simulate a bait-link visit.")
print("Press CTRL+C to stop the server.")
print("======================================")

server = HTTPServer(("127.0.0.1", 8080), HoneyHandler)
server.serve_forever()