import os
from json.decoder import JSONDecodeError
import spotipy.util as util
import spotipy


def get_token(username, scope='', loc='keys.py'):
    from keys import client_id, client_secret
    """ Get spotipy access token with specified scope and keys"""
    redirect_uri = 'http://localhost/'

    try:
        token = util.prompt_for_user_token(username, scope, client_id,
                                           client_secret, redirect_uri)
    except (AttributeError, JSONDecodeError):
        os.remove(f".cache-{username}")
        token = util.prompt_for_user_token(username, scope, client_id,
                                           client_secret, redirect_uri)

    return token

def spotify_login():
    """Function to loginto hrkp's spotipy"""

    # Get access token
    token = get_token('hrkp',
                      scope='user-modify-playback-state playlist-read-private\
                      user-modify-private')

    sp = spotipy.Spotify(auth=token)
    return sp