import spotipy
import spotipyFuncs as msp
import numpy as np
import pandas as pd

n_songs = 10

# Load spreadsheet
weightings=pd.read_excel('weightings.xlsx')

# Calculate total of weightings for normalisation
total_weight = weightings['Weighting'].sum()
# Normalise weightings to probability (p=weighting/total_weight)
probs = weightings['Weighting']/total_weight

ids = list(weightings['URI'])
new_ids = []

# Sample n_songs without replacement with probability probs
for idx in range(n_songs):
    new_ids.append(np.random.choice(ids, p=probs))

# loginto spotify
# Get access token
token = msp.get_token('hrkp',
                      scope='user-modify-playback-state playlist-read-private\
                      user-modify-private')

# shuffler_playlist URI
playlist_uri = 'spotify:user:hrkp:playlist:097gO1u0aaAjH0u2lX1Ylg'

sp = spotipy.Spotify(auth=token)

# Play shuffled songs
sp.start_playback(uris=new_ids)