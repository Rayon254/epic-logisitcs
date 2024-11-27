from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    
    fullname = emailaddress = message = None

    if request.method == 'POST':
       
        fullname = request.form.get('firstname')
        emailaddress = request.form.get('emailaddress')
        message = request.form.get('message')


    return render_template(
        'index.html',
        fullname=fullname,
        emailaddress=emailaddress,
        message=message
    )
if __name__ == "__main__":
    app.debug = True
    app.run(port=5000)






