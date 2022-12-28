from flask import Flask, render_template, request
import random
import string

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

    password = ''.join(random.sample(password_chars, k=length))
    return password


@app.route('/')
def index():
    password = generate_password(6, True, True, True, True)
    return render_template('index.html', password=password)


@app.route('/', methods=['POST'])
def generate_password_route():
    length = int(request.form['length'])
    uppercase = request.form.get('uppercase') == '1'
    lowercase = request.form.get('lowercase') == '1'
    numbers = request.form.get('numbers') == '1'
    symbols = request.form.get('symbols') == '1'
    password = generate_password(length, uppercase, lowercase, numbers, symbols)
    return render_template('index.html', password=password)


if __name__ == '__main__':
    app.run()
