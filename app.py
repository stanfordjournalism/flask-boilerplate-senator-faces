from flask import Flask
from flask import render_template
from helpers.legislators import get_senators, find_senator_by_id

from os.path import exists

app = Flask(__name__)

@app.route("/hello")
def helloworld():
    return render_template('hello.html')

@app.route('/press-releases/<name_of_press_release>')
def trump(name_of_press_release):
    filename = 'helpers/templates/' + name_of_press_release + '.html'
    if exists(filename):
        return render_template(name_of_press_release + '.html')
    else:
        return """
        <div class="page-not-found__background-image" style="background-image:url('https://assets.bwbx.io/business/public/images/bbiz404-d662b65a97.gif');"></div>
        """
@app.route("/")
def homepage():
    return render_template('index.html')

@app.route("/senators")
def senators():
    return render_template('senators.html', senators=get_senators())


@app.route("/senators/<bio_id>")
def senator_profile(bio_id):
    senator = find_senator_by_id(bio_id)
    if senator:
        return render_template('senator.html', senator=senator)
    else:
        return "Senator with bioguide ID {} could not be found".format(bio_id)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
