from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

# reCAPTCHA settings
RECAPTCHA_SITE_KEY = '6LdQiJ0qAAAAALcrQ7rGVb7WhtZSwCcNa8u_2QTw'
RECAPTCHA_SECRET_KEY = '6LdQiJ0qAAAAAPc9JXFnOsB-o4GzoFh0jYIG1PO3'

@app.route('/')
def index():
    return render_template('captcha.html', recaptcha_site_key=RECAPTCHA_SITE_KEY)

@app.route('/verify', methods=['POST'])
def verify():
    data = {
        'secret': RECAPTCHA_SECRET_KEY,
        'response': request.form['g-recaptcha-response']
    }
    response = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
    result = response.json()

    if result['success']:
        return redirect('/rotate')
    else:
        return "reCAPTCHA verification failed, please try again."

@app.route('/rotate')
def hello_world():
    return render_template("root.html")

if __name__ == '__main__':
    app.run()