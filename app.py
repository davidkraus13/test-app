from flask import Flask
app = Flask(__name__)


@app.get('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()

    print("aasasd")
