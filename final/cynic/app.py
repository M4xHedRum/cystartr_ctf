from flask import Flask, request, jsonify, make_response, render_template, redirect, url_for
from random import randint
import jwt
import json
from base64 import b64decode

app = Flask(__name__)
app.config['SECRET_KEY'] = 'breakingtheworldletsgooooo'

@app.route('/', methods=['GET'])
def login():
    jwt_cookie = request.cookies.get('jwt')
    if not jwt_cookie:
        # Set a new JWT cookie with username "guest" using HS256
        payload = {'username': "guest"+str(randint(1,10000000000)), 'amount': 10000, 'flag':0}
        jwt_cookie = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
        response = make_response('Welcome to my /artshop')
        response.set_cookie('jwt', value=jwt_cookie)
        return response
    return redirect(url_for('artshop'))

@app.route('/artshop', methods=['GET', 'POST'])
def artshop():
    jwt_cookie = request.cookies.get('jwt')
    if not jwt_cookie:
        return redirect(url_for('login'))        
    try:
        payload = jwt.decode(jwt_cookie, app.config['SECRET_KEY'], algorithms=['HS256'])
        user_name = payload["username"]
        user_balance = payload["amount"]
        user_flag = payload["flag"]
    except:
        return "Invalid Token"
    if request.method == "POST":
        flag = request.form.get("flag", "")
        if "18000" not in flag:
            return "18000 not in purchase amt"
        try:
            flag = int(flag)
        except:
            return "Invalid Amount"
        if user_balance > flag:
            payload["amount"] = user_balance - flag
            payload["flag"] = "DoHCTF{Look_out_for_int_overflow}"
            new_jwt_token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
            response = make_response("Purchased")
            response.set_cookie('jwt', value=new_jwt_token)
            return response
        else:
            return "Too broke to purchase"
    else:
        return render_template("artshop.html", user_name = user_name, user_balance = user_balance)

@app.route('/robots.txt', methods=['GET'])
def robots():
    return("Fine!<br>/<br>/artshop")


if __name__ == '__main__':
    app.run()
