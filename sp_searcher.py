import spotipy
import json
import os
import sys
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID = os.getenv('CLIENT_ID', '')
CLIENT_SECRET = os.getenv('CLIENT_SECRET', '')

# playlist_id = sys.argv[1] # Argument passed on command line

# file_path = sys.argv[2] # File path to save results

client_credentials_manager = SpotifyClientCredentials(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET
)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

searchQuery = input(">>> Insert the URI of the playlist: ").split(":")

searchResults = sp.user_playlist_tracks(searchQuery[2], searchQuery[4], fields='items')
print()


ids = []

for item in searchResults["items"]:
    ids.append(item["track"]["id"])


features = sp.audio_features(ids)

print(json.dumps(features, sort_keys=True, indent=4))


# with open(file_path, 'w') as f:
#     json.dump(playlist['tracks'], f, indent=2)
#     print('FINISH')