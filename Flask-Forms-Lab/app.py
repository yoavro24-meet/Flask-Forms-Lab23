from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "yoav"
password = "124"
facebook_friends=["Loai","Kenda","Avigail", "George", "Fouad", "Gi"]


@app.route('/')  # '/' for the default page
def login():
	return render_template('login.html')

@app.route('/login',methods = ["GET",'POST'])
def crdntal():
	if request.method == 'POST':
		username2 = request.form['username']
		password2 = request.form['password']  

		if username2 == username and password2 == password:
			return redirect(url_for('home'))
	else:
		return render_template('login.html')

@app.route('/home')
def home():
	return render_template('home.html',fbf = facebook_friends)

@app.route('/friend_exists/<string:name>')
def friend_exists(name):
	return render_template('friend_exists.html', n = name in facebook_friends)
	


if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
		debug=True
	)
