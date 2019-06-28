import spotipy
import json
import os
import sys
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID = os.getenv('CLIENT_ID', '')
CLIENT_SECRET = os.getenv('CLIENT_SECRET', '')

playlist_id = sys.argv[1] # Argument passed on command line

file_path = sys.argv[2] # File path to save results

client_credentials_manager = SpotifyClientCredentials(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET
)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

playlist = sp.user_playlist('Spotify', playlist_id=playlist_id)

with open(file_path, 'w') as f:
    json.dump(playlist['tracks'], f, indent=2)
    print('FINISH')