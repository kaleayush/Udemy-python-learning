from flask import Flask, render_template
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

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    # run the application on the local development server
    app.run(debug=True)