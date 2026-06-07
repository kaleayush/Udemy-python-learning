from flask import Flask, render_template, request
# creating instance of Flask class
# which will be our WSGI application

#WSGI application
# why we pass __name__ as argument to Flask class?
# The __name__ variable is a special Python variable that holds the name of the current module.
# When you create an instance of the Flask class, you typically pass __name__ as an argument to it.
#  This is because Flask uses this information to determine the 
# root path of the application and to locate resources such as templates and static files.

app = Flask(__name__)

@app.route('/')
def Welcome():
    return 'Welcome to Flask application. this should be the home page of the application. kmsd'

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET','POST'])
def contact():
    if request.method == 'POST':
        pass 
        # handle form submission
        name = request.form['name']
        email = request.form['email']
        print(f"Received contact form submission from {name} ({email})")
        # message = request.form['message']
        # do something with the form data, such as save it to a database or send an email
    return render_template('contact.html')

@app.route('/submit', methods=['POST'])
def Submit():
    # handle form submission
    name = request.form['name']
    email = request.form['email']
    print(f"Received contact form submission from {name} ({email})")
    return render_template('submit.html')
    # message = request.form['message']
    # do something with the form data, such as save it to a database or send an email


if __name__ == '__main__':
    # run the application on the local development server
    app.run(debug=True)