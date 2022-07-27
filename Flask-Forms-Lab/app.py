from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "llo2ay"
password = "123"
facebook_friends=["Loai","Yonathan","Adan", "George", "Fouad", "Celina"]


@app.route('/', methods=['GET', 'POST'])  # '/' for the default page
def login():
	if request.method== 'POST':
		if name==username
  else:
  	print("try again")

  return render_template('login.html')

@app.route('/home')
def home(facebook_friends[]):
	return render_template('home.html'facebook_frieands=facebook_frieands)



 
  



if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)