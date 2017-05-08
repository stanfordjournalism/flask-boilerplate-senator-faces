from flask import Flask
from flask import render_template
from helpers.foo import get_senators, get_senator

app = Flask(__name__)

@app.route("/hello")
def helloworld():
    return render_template('hello.html')

@app.route("/")
def homepage():
    return render_template('index.html', senators=get_senators())

@app.route("/senators/<bio_id>")
def senator_profile(bio_id):
    senator = get_senator(bio_id)
    return render_template('senator.html', senator=senator)



if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
