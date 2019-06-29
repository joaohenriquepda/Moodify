from flask import Flask, jsonify, request
import spotipy
import spotipy.util as util
from spotipy import oauth2
import os

SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID', '')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET', '')
SPOTIPY_REDIRECT_URI = 'http://localhost:5000/emotion/'

app = Flask(__name__)

sp_oauth = oauth2.SpotifyOAuth(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET,SPOTIPY_REDIRECT_URI, scope='user-read-recently-played')

@app.route('/ask-auth/<username>')
def ask_auth(username):
    savedToken = util.prompt_for_user_token(username, scope='user-read-recently-played')

@app.route('/emotion/')
def emotion():
    code = request.args.get('code')
    token_info = sp_oauth.get_access_token(code)
    access_token = token_info['access_token']

    if access_token:
        sp = spotipy.Spotify(access_token)
        last10 = sp.current_user_recently_played(10)
        last50 = sp.current_user_recently_played(50)

        ids10 = []
        ids50 = []

        for music in last10['items']:
            ids10.append(music['track']['id'])

        for music in last50['items']:
            ids50.append(music['track']['id'])

        features10 = sp.audio_features(ids10)
        features50 = sp.audio_features(ids50)

        for element in features10:
            if type(element) is dict:
                del element["type"]
                del element['analysis_url']
                del element['duration_ms']
                del element['track_href']
                del element['uri']

        for element in features50:
            if type(element) is dict:
                del element["type"]
                del element['analysis_url']
                del element['duration_ms']
                del element['track_href']
                del element['uri']

        response = {
            'status': 'success',
            'data' : {
                'last10': features10,
                'last50': features50
            }
        }

    else:
        response = {
            'status': 'fail',
            'data': {}
        }
    
    return jsonify(response)
