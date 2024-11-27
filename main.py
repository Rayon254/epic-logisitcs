from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.secret_key = 'ksfgj'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print("Form submitted")
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        emailaddress = request.form.get('emailaddress')
        phonenumber = request.form.get('phonenumber')
        
        # Print the received form data to the console
        print(f"Received data: {firstname}, {lastname}, {emailaddress}, {phonenumber}")
        
        return render_template('index.html', firstname=firstname, lastname=lastname,
                               emailaddress=emailaddress, phonenumber=phonenumber)
    
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=5001)

