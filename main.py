from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    
    name = email = message = None

    if request.method == 'POST':
       
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')


    return render_template(
        'index.html',
        name=name,
        email=email,
        message=message
    )
if __name__ == "__main__":
    app.debug = True
    app.run(port=5000)






