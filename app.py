from flask import Flask, make_response, render_template, request
import random
import string
import os

app = Flask(__name__)


def generate_password(length, uppercase, lowercase, numbers, symbols):
    password_chars = ''
    if uppercase:
        password_chars += string.ascii_uppercase
    if lowercase:
        password_chars += string.ascii_lowercase
    if numbers:
        password_chars += string.digits
    if symbols:
        password_chars += string.punctuation

    password = ''.join(random.choices(password_chars, k=length))
    return password


@app.route('/')
def index():
    template = render_template('index.html')
    response = make_response(template)
    response.headers['Cache-Control'] = 'public, max-age=300, s-maxage=600'
    return response


@app.route('/', methods=['POST'])
def generate_password_route():
    if request.method == 'POST':
        length = 0
        if request.form['length'] is None or request.form['length'] == '':
            length = 6
        length = int(request.form['length'])
        uppercase = request.form.get('uppercase') == '1'
        lowercase = True
        numbers = request.form.get('numbers') == '1'
        symbols = request.form.get('symbols') == '1'
        newPassword = generate_password(
            length, uppercase, lowercase, numbers, symbols)
        return render_template('index.html', newPassword=newPassword)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
