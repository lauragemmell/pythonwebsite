import mandrill

from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)
mandrill_client = mandrill.Mandrill('7FXR83a8RJiIs-1R8Aq7oQ')

@app.route("/home")
def home():
	return render_template('index.html')

@app.route("/applicant/signup")
def applicant_signup():
	return render_template('signup.html')

@app.route("/signup", methods=['POST'])
def sign_up():
	form_data = request.form

	email= form_data['email']
	name= form_data['name']

	mandrill_client.messages.send(
	message={
		'subject': 'Thanks for signing up',
		'from_email': 'chayseldenashby@gmail.com',
		'to': [
			{
				'email': email
			}
		],
		'html': '<p> Welcome to JobSwipe, {0}. You are now ready to take the next step to your dream job </p>'.format(name)
	},
	async=False
	)

	return "Thanks for signing up. Please check your inbox for your confirmation email"

@app.route("/applicant/interface")
def applicant_interface():
	return render_template('applicant_interface.html')

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000, debug=True)

#127.0.0.1