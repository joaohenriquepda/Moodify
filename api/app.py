from flask import Flask, jsonify, request
import spotipy
import spotipy.util as util
from spotipy import oauth2

SPOTIPY_CLIENT_ID = '3732fdd031c94c79aadf7547f007f7e7'
SPOTIPY_CLIENT_SECRET = 'c6714347a13e40e0b3ee14e14b4df7f4'
SPOTIPY_REDIRECT_URI = 'http://localhost:5000/emotion/'

app = Flask(__name__)

sp_oauth = oauth2.SpotifyOAuth(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET,SPOTIPY_REDIRECT_URI, scope='user-read-recently-played')

@app.route('/ask-auth/<username>')
def ask_auth(username):
    savedToken = util.prompt_for_user_token(username, scope='user-read-recently-played')

# @app.route('/emotion/<token>')
# def emotion(token):
#     if token:
#         sp = spotipy.Spotify(auth=token)
#         last10 = sp.current_user_recently_played(10)
#         last100 = sp.current_user_recently_played(100)
#         last1000 = sp.current_user_recently_played(1000)

#         response = {
#             'status': 'success',
#             'data' : {
#                 'last10': [music.to_json() for music in last10],
#                 'last100': [music.to_json() for music in last100],
#                 'last1000': [music.to_json() for music in last1000]
#             }
#         }

#     else:
#         response = {
#             'status': 'fail',
#             'data': {}
#         }
    
#     return jsonify(response)

@app.route('/emotion/')
def emotion():
    code = request.args.get('code')
    token_info = sp_oauth.get_access_token(code)
    access_token = token_info['access_token']

    if access_token:
        sp = spotipy.Spotify(access_token)
        last10 = sp.current_user_recently_played(10)
        last50 = sp.current_user_recently_played(50)

        # response = {
        #     'status': 'success',
        #     'data' : {
        #         'last10': last10,
        #         'last50': last50
        #     }
        # }

    else:
        response = {
            'status': 'fail',
            'data': {}
        }
    
    return jsonify(response)
