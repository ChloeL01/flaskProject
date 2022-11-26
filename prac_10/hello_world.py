from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    """Print hello world."""
    return "<h1>Hello World :)</h1>"


# @app.route('/greet')  # old
# def greet():
#     return "Hello"


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    """Print greeting."""
    return f"Hello {name}"


@app.route('/<celsius>')
def main(celsius):
    """Convert temperature."""
    fahrenheit = convert_to_fahrenheit(float(celsius))
    return f"celsius: {celsius} converted to fahrenheit: {fahrenheit}"


def convert_to_fahrenheit(celsius):
    """Convert fahrenheit to celsius"""
    return celsius * 9.0 / 5 + 32


if __name__ == '__main__':
    app.run()
