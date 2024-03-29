import spotipy
import spotipyFuncs as msp
import numpy as np
import pandas as pd
import argparse

# Create arguement parser
parser = argparse.ArgumentParser()
# Accept number of songs as input
parser.add_argument("--n_songs", type=int,
                    help="Number of songs in playlist",
                    default = 10)

args = parser.parse_args()


# Load spreadsheet
weightings=pd.read_excel('weightings.xlsx')

# Calculate total of weightings for normalisation
total_weight = weightings['Weighting'].sum()
# Normalise weightings to probability (p=weighting/total_weight)
probs = weightings['Weighting']/total_weight

ids = list(weightings['URI'])

# Sample n_songs without replacement with probability probs
new_ids = np.random.choice(ids, size=args.n_songs, p=probs, replace=False)

# Loginto spotipy
sp = msp.spotify_login()

# Play shuffled songs
sp.start_playback(uris=list(new_ids))