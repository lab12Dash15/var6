from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

# reCAPTCHA settings
RECAPTCHA_SITE_KEY = '6LespZ0qAAAAAGu8phR_6bqIR7Swu3E3cGmEvshd'
RECAPTCHA_SECRET_KEY = '6LespZ0qAAAAAC_b3eV9ZUJYIFfBTBlkBWQYNJo1'

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
        return render_template("root.html")
    else:
        return redirect('/')

if __name__ == '__main__':
    app.run()