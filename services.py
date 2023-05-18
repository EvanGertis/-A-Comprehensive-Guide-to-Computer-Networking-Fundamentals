from flask import Flask, request

app = Flask(__name__)

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form['name']
    return f'Hello, {name}!'

if __name__ == '__main__':
    app.run(debug=True)