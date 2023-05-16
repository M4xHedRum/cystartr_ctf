import base64
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

def base64_padding(encoded):
    while len(encoded) % 4 != 0:
        encoded += "="
    return encoded

@app.route('/')
def index():
    return redirect(url_for('xor_route', moon="GgoXAQ4QGxMCHA4ZA1JKDFlWAEFRG1YQGw", sun="c2RzZHZ5dXdnZGd3ZzcyZTcyZTk4dTJ1Yw"))

@app.route('/<moon>/<sun>')
def xor_route(moon, sun):
    if not (moon and sun):
        redirect(url_for('index'))
    try:
        moon = base64.b64decode(base64_padding(moon)).decode("ascii")
        sun = base64.b64decode(base64_padding(sun)).decode("ascii")
    except Exception:
        redirect(url_for('index'))
    result = ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(moon, sun))
    if result == "letterletterletterletterletter":
        return render_template("place.html", page_name ="letter")
    elif result == "flagflagflagflagflag":
        return "DoHCTF{xor_rox_xor}"
    elif result == "indexindexindexindexindex":
        return render_template("place.html",page_name ="index")
    elif result == "aboutaboutaboutaboutabout":
        return render_template("place.html", page_name ="about")
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    print("Use wsgi.py instead")
