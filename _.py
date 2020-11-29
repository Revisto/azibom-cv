"""The Azibom website"""
from flask import (
    Flask,
    request,
    render_template,
    session,
    redirect,
    abort,
    url_for,
    flash,
)

app = Flask(__name__, template_folder="templates", static_folder="static")
app.secret_key = b"n2#)!6=-qv7w7j8wlh_3a$di*j#g5kh&8w8-!9((pzny_p*0v+"


@app.route("/")
def index():
    """ The main page of Resume. """

    return render_template("index.html")


@app.route("/<name>")
def social_media(name):
    """ The Redirect to social medias page """
    data = {
        'twitter':'https://twitter.com/theazibom',
        'linkedin':'https://www.linkedin.com/in/mrsh/',
        'github':'https://github.com/azibom',
        'devto':'https://dev.to/azibom',
        'stack':'https://stackoverflow.com/users/13060981/azibom',
        'stackoverflow':'https://stackoverflow.com/users/13060981/azibom'
    }
    try: 
        redirection_data = data[name.lower()]
        return redirect(redirection_data,code=302)
    except:
        return redirect('/')

if __name__ == "__main__":
    app.run( debug=True)
