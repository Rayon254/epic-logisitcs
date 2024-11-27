from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    
    firstname = lastname = emailaddress = phonenumber = None

    if request.method == 'POST':
       
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        emailaddress = request.form.get('emailaddress')
        phonenumber = request.form.get('phonenumber')

  

    return render_template(
        'index.html',
        firstname=firstname,
        lastname=lastname,
        emailaddress=emailaddress,
        phonenumber=phonenumber
    )
if __name__ == "__main__":
    app.debug = True
    app.run(port=5000)






