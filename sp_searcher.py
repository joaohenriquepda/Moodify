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
    searchQuery = input().split(":")

    if searchQuery[0] == "0":
        break

    else:
        sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

        searchResults = sp.user_playlist_tracks(searchQuery[2], searchQuery[4], fields='items')

        for item in searchResults["items"]:
            print(item['track']['id'])
            ids.append(item["track"]["id"])

ids_set = set(ids)
print('-------------------')
print(ids_set)
ids_set.remove(None)

for item in ids_set:
    print(item)
    features.append(sp.audio_features(item))

print('-------------------')

with open(file_path, 'w') as f:
    json.dump(features, f, indent=2)
    print('FINISH')