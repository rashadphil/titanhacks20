from flask import Flask, render_template, request, redirect, session, url_for
from flask import send_file, make_response, send_from_directory

app = Flask(__name__, template_folder="templates", static_url_path='/static')
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['DEBUG'] = True


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
