from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Name: Kuunal | AppID: 2410286"

if __name__ == '__main__':
    app.run()