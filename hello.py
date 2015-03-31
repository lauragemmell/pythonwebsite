from flask import Flask
from flask import render_template
from flask import request
import mandrill

app = Flask(__name__)

@app.route("/home")
def home():
	return render_template('index.html')

@app.route("/about/why")
def about_why():
	return render_template('about_why.html')

@app.route("/about/how")
def about_how():
	return render_template('about_what.html')

@app.route("/about/team")
def about_team():
	return render_template('about_the_team.html')

@app.route("/contact")
def contact():
	return render_template('contact.html')

@app.route("/blog")
def blog():
	return render_template('blog.html')

@app.route("/companies")
def companymain():
	return render_template('companysignup.html')

@app.route("/companies/signup")
def company_sign_up_page():
	return render_template('companysignup.html')

@app.route("/companies/signin")
def company_sign_in():
	return render_template('companysignin.html')

@app.route("/companies/signin/successful")
def company_sign_in_success():
	return render_template('companysignin_successful.html')

@app.route("/company/signup/complete",methods=['POST'])
def company_sign_up():
	form_data = request.form
	mandrill_client = mandrill.Mandrill('9FdJjzfupPJojkDcNiv4jA')
 	mandrill_client.messages.send(
    message={
        'html': '<p>Hello from Mandrill!</p>',
        'from_email': 'laura-gemmell@hotmail.com',
        'from_name': 'START-UP SEARCH',
        'to': [{'email': form_data['email'], 'name': form_data['name'], 'type': 'to'}],
        "subject": 'Confirmation of START-UP SEARCH sign up'
    }
)
	return render_template('companiessignedup.html')

@app.route("/applicant")
def applicantmain():
	return render_template('applicant_signup.html')
	

@app.route("/applicant/signup")
def applicant_signup():
	return render_template('applicant_signup.html')

@app.route("/applicant/signup/complete", methods=['POST'])
def sign_up():
	form_data = request.form
	mandrill_client = mandrill.Mandrill('7FXR83a8RJiIs-1R8Aq7oQ')
	email= form_data['email']
	name= form_data['name']

	mandrill_client.messages.send(
	message={
		'subject': 'Thanks for signing up to GradBOX',
		'from_email': 'chayseldenashby@gmail.com',
		'to': [
			{
				'email': email
			}
		],
		'html': '<p> Welcome to GradBOX, {0}. You are now ready to take the next step to your dream job </p>'.format(name)
	},
	async=False
	)

	return render_template('applicant_signedup.html')

@app.route("/applicant/signin")
def applicant_signin():
	return render_template('applicant_signin.html')

@app.route("/applicant/interface")
def applicant_interface():
	return render_template('applicant_interface.html')
		
if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000,debug=True)