from flask import Flask
import requests
app = Flask(__name__)

@app.route('/')
def home():
    r = requests.get("https://www.w3schools.com/")
    s = str(r.status_code)
    return s

if __name__ == '__main__':
    app.run(debug=True)
