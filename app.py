from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Webhook Trigger Success "

if __name__ == '__main__':
    print("Build successful ")