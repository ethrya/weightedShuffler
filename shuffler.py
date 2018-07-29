import spotipy
import spotipyFuncs as msp
import numpy as np

n_songs = 10  # Number of songs to play
new_ids = []  # List for song URIs

# Get access token
token = msp.get_token('hrkp',
                      scope='user-modify-playback-state playlist-read-private\
                      user-modify-private')

# shuffler_playlist URI
playlist_uri = 'spotify:user:hrkp:playlist:097gO1u0aaAjH0u2lX1Ylg'

sp = spotipy.Spotify(auth=token)

shuffler_playlist = sp.user_playlist('hrkp', playlist_id=playlist_uri)[
                                     'tracks']['items']

weight_dict = {}


# Ask user for weight of songs in shuffler_playlist
for track in shuffler_playlist:
    weight = input('Weighting of {}: '.format(track['track']['name']))
    id = track['track']['uri']
    weight_dict[id] = weight

# Create lists of song URIs and normalised weightings
ids = list(weight_dict.keys())
probs = np.array(list(weight_dict.values()))
probs = probs.astype(float)
probs = 1/sum(probs)*probs

# Choose n_songs random songs with PDF from normalised weightings
for idx in range(n_songs):
    new_ids.append(np.random.choice(ids, p=probs))

# Play shuffled songs
sp.start_playback(uris=new_ids)