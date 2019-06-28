import spotipy
import json
import os
import sys
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID = os.getenv('CLIENT_ID', '')
CLIENT_SECRET = os.getenv('CLIENT_SECRET', '')

file_path = sys.argv[1] # File path to save results

client_credentials_manager = SpotifyClientCredentials(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET
)

ids = []
features = []

while True:
    searchQuery = input(">>> Insira o URI da playlist ou 0 para parar a aplicação: ").split(":")
    print(searchQuery)

    if searchQuery[0] == "0":
        break

    else:
        sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

        searchResults = sp.user_playlist_tracks(searchQuery[2], searchQuery[4], fields='items')
        print()

        for item in searchResults["items"]:
            ids.append(item["track"]["id"])

for id in ids:
    features.append(sp.audio_features(id))


with open(file_path, 'w') as f:
    json.dump(features, f, indent=2)
    print('FINISH')