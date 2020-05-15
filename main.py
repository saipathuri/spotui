import tkinter as tk
import spotify_client
from PIL import ImageTk, Image
import requests
import time

MAX_HEIGHT=480
MAX_WIDTH=320

ALBUM_ART_SIZE=300

PADDING=10

DOUBLE_PADDING=2*PADDING

ICON_SIZE=64

#1DB954
DEFAULT_BG = "black"

STATE_PLAY = 1
STATE_PAUSE = 0

def create_icon_button(img, frame):
    button = tk.Button(frame, image=img, bg=DEFAULT_BG, activebackground=DEFAULT_BG, padx=0, pady=0, relief=tk.FLAT, borderwidth=0, highlightthickness=0)
    button.photo = img
    button.pack()
    return button

def play(button):
    global STATE
    if STATE == STATE_PAUSE:
        STATE = STATE_PLAY
        spotify_client.play()
    else:
        STATE = STATE_PAUSE
        spotify_client.pause()
    
    update_play_button(button)

def update_play_button(button):
    global STATE
    if STATE == STATE_PAUSE:
        new_icon = PLAY_ICON
    else:
        new_icon = PAUSE_ICON
    
    button.configure(image=new_icon)
    button.photo = new_icon
        
def skip_song():
    spotify_client.next()
    time.sleep(.15)
    get_and_process_data()

def previous_song():
    spotify_client.previous()
    time.sleep(.15)
    get_and_process_data()

def download_image(url):
    r = requests.get(url)
    with open('art.jpg', 'wb') as f:
        f.write(r.content)

def update_album_art():
    ART = ImageTk.PhotoImage(Image.open("art.jpg"))
    art_holder.configure(image=ART)
    art_holder.image = ART

def get_and_process_data(root):
    global STATE
    data = spotify_client.get_currently_playing()
    images_arr = data['item']['album']['images']
    image_url = list(filter(lambda x: x['height'] == 300, images_arr))[0]['url']
    
    process_new_image(image_url)

    # is_playing = data['is_playing']
    # if is_playing:
    #     STATE = STATE_PLAY
    # else:
    #     STATE = STATE_PAUSE
    # update_play_button(play_pause)

    album_name = data['item']['album']['name']
    artist_name = data['item']['artists'][0]['name']
    track_name = data['item']['name']

    track_label.configure(text=track_name)
    artist_label.configure(text=artist_name)
    album_label.configure(text=album_name)

    root.after(3000, lambda: get_and_process_data(root))

def process_new_image(image_url):
    download_image(image_url)
    update_album_art()

if __name__ == '__main__':
    global STATE
    STATE = STATE_PAUSE
    # Configure window
    root = tk.Tk()
    # root.attributes('-type', 'dock')
    # root.attributes('-fullscreen', True)
    root.geometry(f'{MAX_WIDTH}x{MAX_HEIGHT}')
    root.configure(bg=DEFAULT_BG)
    root.focus_force()

    # Create all icons
    PLAY_ICON = tk.PhotoImage(file='res/play.png')
    PAUSE_ICON = tk.PhotoImage(file='res/pause.png')
    SKIP_ICON = tk.PhotoImage(file='res/skip.png')
    PREVIOUS_ICON = tk.PhotoImage(file='res/previous.png')
    ART = ImageTk.PhotoImage(Image.open("art.jpg"))

    # Create all frames
    album_art_frame = tk.Frame(master=root, width=ALBUM_ART_SIZE, height=ALBUM_ART_SIZE, bg="white")
    album_art_frame.place(x=PADDING, y=PADDING)

    info_frame = tk.Frame(master=root, width=MAX_WIDTH-2*PADDING, height=140, bg=DEFAULT_BG)
    info_frame.pack_propagate(0)
    info_frame.place(relx=PADDING/MAX_WIDTH, rely=.75)
    
    art_holder = tk.Label(album_art_frame, image=ART)
    art_holder.image = ART
    art_holder.pack()

    # play_pause_frame = tk.Frame(master=root, width=ICON_SIZE, height=ICON_SIZE, bg=DEFAULT_BG)
    # play_pause_frame.place(relx=.75, y=MAX_HEIGHT-ICON_SIZE-PADDING)
    
    # skip_frame = tk.Frame(master=root, width=ICON_SIZE, height=ICON_SIZE, bg=DEFAULT_BG)
    # skip_frame.place(relx=.85, y=MAX_HEIGHT-2*ICON_SIZE-PADDING)

    # previous_frame = tk.Frame(master=root, width=ICON_SIZE, height=ICON_SIZE, bg=DEFAULT_BG)
    # previous_frame.place(relx=.65, y=MAX_HEIGHT-2*ICON_SIZE-PADDING)

    # # create all buttons
    # play_pause = create_icon_button(PLAY_ICON, play_pause_frame)
    # play_pause.configure(command= lambda: play(play_pause))

    # skip = create_icon_button(SKIP_ICON, skip_frame)
    # skip.configure(command=skip_song)

    # previous = create_icon_button(PREVIOUS_ICON, previous_frame)
    # previous.configure(command=previous_song)

    # Create track info labels
    INFO_VERTICAL_PADDING = (MAX_HEIGHT-ALBUM_ART_SIZE-2*PADDING)/MAX_HEIGHT
    INFO_VERTICAL_DISTANCE = .05
    track_label = tk.Label(info_frame, text='Track Name', font=("Montserrat", 16, 'bold'), justify=tk.CENTER,  bg=DEFAULT_BG, fg='#FFF')
    track_label.pack(fill=tk.X)

    artist_label = tk.Label(info_frame, text='Artist Name', font=("Montserrat", 14), justify=tk.LEFT, bg=DEFAULT_BG, fg='#FFF')
    artist_label.pack(fill=tk.X)

    album_label = tk.Label(info_frame, text='Album Name', font=("Montserrat", 14), justify=tk.LEFT, bg=DEFAULT_BG, fg='#B1B0AF')
    album_label.pack(fill=tk.X)

    # configure spotify api
    spotify_client.setup()

    # get data
    get_and_process_data(root)

    root.mainloop()