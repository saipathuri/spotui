import spotipy
import settings
import os

username = 'saipathuri'
scopes = 'user-read-currently-playing user-read-playback-state user-modify-playback-state'
token = None
sp = None

def setup():
    global token, sp
    token = spotipy.util.prompt_for_user_token(username, scopes)
    sp = spotipy.Spotify(auth=token)

def get_currently_playing():
    if token and sp:
        return sp.current_playback()
    else:
        raise Exception("Use setup() first")

def next():
    if token and sp:
        return sp.next_track()
    else:
        raise Exception("Use setup() first")

def previous():
    if token and sp:
        return sp.previous_track()
    else:
        raise Exception("Use setup() first")

def pause():
    if token and sp:
        return sp.pause_playback()
    else:
        raise Exception("Use setup() first")
    
def play():
    if token and sp:
        return sp.start_playback()
    else:
        raise Exception("Use setup() first")