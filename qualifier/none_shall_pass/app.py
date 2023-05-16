from flask import Flask, request, jsonify, make_response, render_template
import jwt
import json
from base64 import b64decode

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretpasskeyllol'

flag = "DoHCTF{jwt_has_a_none_algo_loll}"

@app.route('/', methods=['GET'])
def login():
    jwt_cookie = request.cookies.get('jwt')

    if not jwt_cookie:
        # Set a new JWT cookie with username "guest" using HS256
        payload = {'username': 'guest'}
        jwt_cookie = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
        response = make_response('Who are you?')
        response.set_cookie('jwt', value=jwt_cookie)
        return response

    try:
        if jwt.get_unverified_header(jwt_cookie)['alg'] == 'none':
            token_info = jwt_cookie.split(".")[1]
            while len(token_info) % 4 != 0:
                token_info += "="
            decoded = b64decode(token_info).decode('utf-8')
            decoded_dict = json.loads(decoded)
            user = decoded_dict["username"].lower()
            if user == "admin":
                return render_template('index.html', variable=flag)
            return render_template('index.html', variable=f"Who's {user}")

        # Decode the JWT cookie and verify the signature
        payload = jwt.decode(jwt_cookie, app.config['SECRET_KEY'], algorithms=['HS256'])

        # Check if the username is "admin" and algorithm is set to none
        if payload['username'] == 'admin':
            # Return the flag
            return render_template('index.html', variable=flag)
        else:
            return render_template('index.html', variable="Invalid Token")
    except jwt.ExpiredSignatureError:
        return render_template('index.html', variable='Expired Token')
    except jwt.InvalidTokenError:
        return render_template('index.html', variable='Invalid Token')
    except Exception:
        return render_template('index.html', variable='Error')
    return render_template('index.html', variable='Error')
if __name__ == '__main__':
    print("Use wsgi.py instead")
