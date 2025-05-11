from flask import Flask

app = Flask(__name__)

@app.route("/api")
def hello_world():
    return 'Hello, World!'

@app.route("/hello")
def hello():
    return "<h1>Hallo</h1>"

@app.route("/25-01")
def klasse():
    return "Grüße an die Klasse 25-01!"

@app.route("/about")
def about():
    return "Willkommen auf der ABOUT-Seite! Hier erfährst du mehr über uns."

@app.route("/info")
def info():
    return "Das ist eine INFO-Seite über Hunde-Salons 🐶✂️"

if __name__ == "__main__":
    app.run(debug=True)
