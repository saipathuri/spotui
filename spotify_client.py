import spotipy
import settings
import os
from spotipy.exceptions import SpotifyException

username = 'saipathuri'
scopes = 'user-read-currently-playing user-read-playback-state user-modify-playback-state'
token = None
sp = None

def setup():
    global token, sp
    token = spotipy.util.prompt_for_user_token(username, scopes)
    sp = spotipy.Spotify(auth=token)

def get_currently_playing():
    return check_setup(lambda: sp.current_playback())

def next():
    return check_setup(lambda: sp.next_track())

def previous():
    return check_setup(lambda: sp.previous_track())

def pause():
    return check_setup(lambda: sp.pause_playback())
    
def play():
    return check_setup(lambda: sp.start_playback())

def check_setup(func):
    if token and sp:
        try:
            return func()
        except SpotifyException:
            print("Spotify Exception, rerunning setup")
            setup()
            return func()
    else:
        raise Exception("Use setup() first")