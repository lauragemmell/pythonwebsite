from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
import mandrill
import random
import string
from random import randint

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
	mandrill_client = mandrill.Mandrill('ZJ6h81vltJ7rGe7axB02cg')
 	template_content = [{'content': form_data['name'], 'name': 'name'}, {'content': (form_data['name']).replace(" ", "").lower() + str(randint(100,999)), 'name': 'username'}, {'content': ''.join(random.choice(string.ascii_letters + string.digits) for i in range (12)), 'name': 'password'}] 
	response = mandrill_client.messages.send_template(
		template_name = 'companyemail',
		template_content = template_content,
		message = {
		'subject': 'Welcome to GradBOX',
		'from_email': 'welcome@gradbox.com',
		'to': [{'email': form_data['email'], 'name': form_data['name'], 'type': 'to'}],
	
		},
		async = False
	)
	return render_template('companiessignedup.html')

@app.route("/applicant")
def applicantmain():
	return render_template('applicant_signup.html')
	

@app.route("/applicant/signup")
def applicant_signup():
	return render_template('applicant_signup.html')

@app.route("/applicant/signup/complete", methods=['POST'])
def applicant_sign_up():
	form_data = request.form
	mandrill_client = mandrill.Mandrill('ZJ6h81vltJ7rGe7axB02cg')
 	template_content = [{'content': form_data['name'], 'name': 'name'}, {'content': (form_data['name']).replace(" ", "").lower() + str(randint(100,999)), 'name': 'username'}, {'content': ''.join(random.choice(string.ascii_letters + string.digits) for i in range (12)), 'name': 'password'}] 
	response = mandrill_client.messages.send_template(
		template_name = 'useremail',
		template_content = template_content,
		message = {
		'subject': 'Welcome to GradBOX',
		'from_email': 'welcome@gradbox.com',
		'to': [{'email': form_data['email'], 'name': form_data['name'], 'type': 'to'}],
	
		},
		async = False
	)

	return render_template('applicant_signedup.html')

@app.route("/applicant/signin")
def applicant_signin():
	return render_template('applicant_signin.html')

@app.route("/applicant/interface")
def applicant_interface():
	return render_template('applicant_interface.html')

@app.route("/applicant/jobinator")
def job_gen():
	return render_template('job_gen.html')

@app.route("/applicant/jobinator/result", methods=['POST'])
def job_gen_result():
	form_data = request.form
	Enjoy = form_data['Enjoy']
	Interests = form_data['Interests']
	Vibe = form_data['Vibe']
	Colour = form_data['Colour']
	Animal = form_data['Animal']

	if Interests == "Gaming":
		Company="mobile gaming company"
	elif Interests == "Fashion":
		Company="trend analysis start up"
	elif Interests == "Nature":
		if Enjoy == "Active":
			Company = "marine conservation unit"
		else: 
			Company = "enviromental NGO"
	elif Interests == "Sport":
		Company = "sponsorship valuation agency"
	elif Interests == "Film":
		Company = "a YouTube talent management company"
	else:
		Company="start up"

	if Enjoy == "Active":
		role = "field worker"
	else:
		role = Enjoy

	if Vibe == "chilled":
		if Enjoy == "Active":
			Office = "with its offices outside the city"
		else:
			Office = "with big, airy, open-plan offices"
	elif Vibe == "freedom":
		if Enjoy == "graphic designer":
			Office = "where you can work from wherever makes you feel inspired"
		elif Enjoy == "support team worker":
			Office = "where you can fit your work around your other commitments"	
		else:
			Office = "where you can work from wherever you want and to your own schedule"
	elif Vibe == "busy":
		Office = "where there is always something going on"
	elif Vibe == "social":
		if Interests == Sport:
			Office = "where there is a company football team"
		else:
			Office = "with a great office culture"
	elif Vibe == "pressure":
		Office = "where there is always plenty of work to keep busy with"
	
	return render_template('job_gen_result.html', Company=Company, role=role, Office=Office, Animal=Animal)
		
if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000,debug=True)