from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/hello/<name>")
def hello(name):
	return render_template('hello2.html', name= name)

@app.route("/signup",methods=['POST'])
def sign_up():
	form_data = request.form
	print form_data['name']
	print form_data['email']
	return "All OK"

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000,debug=True)