import spotipy
import spotipyFuncs as msp
import numpy as np
import pandas as pd

# Login to spotify
sp = msp.spotify_login()

# shuffler_playlist URI
playlist_uri = 'spotify:user:hrkp:playlist:097gO1u0aaAjH0u2lX1Ylg'

shuffler_playlist = sp.user_playlist('hrkp', playlist_id=playlist_uri)[
                                     'tracks']['items']

# Create empty data frame for
colNames = ["Artist", "Album", "Title", "Weighting", "URI"]
playlist_frame = pd.DataFrame(columns=colNames)

# Populate data frame from playlist
for song in shuffler_playlist:
    song = song['track']
    songFrame = pd.DataFrame([[song['artists'][0]['name'], song['album']['name'],
    song['name'],5, song['uri']]], columns=["Artist", "Album", "Title", "Weighting", "URI"])
    playlist_frame = playlist_frame.append(songFrame)

# Save as excel file
writer = pd.ExcelWriter('weightings.xlsx')
playlist_frame.to_excel(writer,index=False)