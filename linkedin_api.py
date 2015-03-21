from linkedin import linkedin

#from flask import Flask
#from flask import render_template
#from flask import request

#app = Flask(__name__)


API_KEY = '77ixeb51nc5pb5'
API_SECRET = 'lOkeJpombJS8wSyT'
RETURN_URL = 'http://127.0.0.1/signup'

authentication = linkedin.LinkedInAuthentication(API_KEY, API_SECRET, RETURN_URL, linkedin.PERMISSIONS.enums.values())
# Optionally one can send custom "state" value that will be returned from OAuth server
# It can be used to track your user state or something else (it's up to you)
# Be aware that this value is sent to OAuth server AS IS - make sure to encode or hash it
#authorization.state = 'your_encoded_message'
print authentication.authorization_url  # open this url on your browser
application = linkedin.LinkedInApplication(authentication)

authentication.authorization_code = 'AQTGaJoHf9flbbgGxgKDKyZDbC1u44qqLBWmPwrliEx0OPqbE7zoO9ZMwxa0y49bEeV-nu5kuf28Gm-L6vVSoSHSlGVQ_1hkiK3UH-LZCg8wjg0NeHM'
authentication.get_access_token()

#@app.route("/signup")

#if __name__ == "__main__":
#	app.run(host="0.0.0.0", port=5000, debug=True)


#127.0.0.1