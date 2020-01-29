from flask import Flask, request, redirect, render_template
import random
from database import *
from flask_mail import Mail
from flask_mail import Message
app = Flask(__name__)
#For the contact us
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'danielleweiss171@gmail.com'
app.config['MAIL_DEFAULT_SENDER'] = 'danielleweiss171@gmail.com'
app.config['MAIL_PASSWORD'] = 'danielle171'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
@app.route('/')
def index():
	allv =[]
	allv= everything()
	return render_template('home.html',data=allv)
@app.route('/contact',methods = ['GET','POST']) 
def contact():
	if request.method == 'POST':
		msg = Message('Roads',recipients=['danielleweiss171@gmail.com'])
		msg.html = request.form['address'] + " says:<br>"+request.form['message']
		mail.send(msg)
		
	return render_template('contact.html')
if __name__ == '__main__':
	app.run(debug = True)