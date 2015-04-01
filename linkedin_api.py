from SocketServer import ThreadingTCPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
from webbrowser import open_new_tab
from json import dumps
from urlparse import urlparse
from os import environ
from types import NoneType

from linkedin.linkedin import LinkedInAuthentication, LinkedInApplication, PERMISSIONS

from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

API_KEY = '77oeww4ifjp1x9'
API_SECRET = 'HNNb1j54d3mbOcsz'
RETURN_URL = 'http://localhost:5000/linkedin'
authentication = LinkedInAuthentication(API_KEY, API_SECRET, RETURN_URL, PERMISSIONS.enums.values())
application = LinkedInApplication(authentication)

application = LinkedInApplication(token="AQVvfw_sneGeFn3LMqlsPy8N1LirvyyW33BgpyurHZmw9usW0jAIA_fG-6p4qFag4XiRNp2dieKWCOZHBC0RJIDEFaYbV_qK5k3xSm-T5t5cx9xI6xN4PD5p3hhetjpsvtt0OQSn0QlgmJNXapJHyFUvbKYuBKhQtaHcJW72z1_gn21h8cA")


application.get_profile()

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000, debug=True)


#127.0.0.1