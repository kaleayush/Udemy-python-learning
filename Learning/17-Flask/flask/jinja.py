import math

from flask import Flask, redirect, render_template, request, redirect, url_for
# creating instance of Flask class
# which will be our WSGI application

'''
{{}} expression delimiters: used to evaluate and display the value of a variable or an expression.
{% %} statement delimiters: used to execute control structures such as loops and conditionals.
{# #} comment delimiters: used to add comments to the template that will not be rendered in the final output.

'''


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

# variable rules in Flask routes allow you to capture values from the URL and pass them as arguments to your view functions.
@app.route('/success/<int:score>', methods=['GET','POST'])
def successres(score):
    res = ""
    if score >= 50:
        res = "Passed"
    else:
        res = "Failed"
    exp = {"marks": score, "result": res}
    return render_template('success.html', data=exp , score=score)

# @app.route('/contact', methods=['GET','POST'])
# def contact():
#     return render_template('contact.html')

@app.route('/submit', methods=['POST', 'GET'])
def Submit():
    if request.method == 'POST':
        # handle form submission
        maths = int(request.form['maths'])
        english = int(request.form['english'])
        science = int(request.form['science'])
        total = (maths + english + science)/3 
        return redirect(url_for('successres', score= total))
    else:
        return render_template("subject.html")




if __name__ == '__main__':
    # run the application on the local development server
    app.run(debug=True)