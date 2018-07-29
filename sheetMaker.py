import spotipy
import spotipyFuncs as msp
import sheetFuns as sf
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

# Find pre extisting spreadsheet
originalSheet = sf.load_sheet()

# Populate data frame from spotify playlist
for song in shuffler_playlist:
    # Data associated with song
    song = song['track']

    # If the song is in orginalSheet using preexting weighting otherwise set it to 5
    try:
        originalSheet['URI'].str.contains(song['uri'])
        weight = originalSheet['Weighting'][originalSheet['URI']==song['uri']].iloc[0]
    except TypeError and IndexError:
        weight = 5
    
    # Add song to new dataframe
    songFrame = pd.DataFrame([[song['artists'][0]['name'], song['album']['name'],
    song['name'], weight, song['uri']]], columns=colNames)
    playlist_frame = playlist_frame.append(songFrame)

# Save as excel file
writer = pd.ExcelWriter('weightings.xlsx')
playlist_frame.to_excel(writer,index=False)