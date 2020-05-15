import tkinter as tk

MAX_HEIGHT=320
MAX_WIDTH=480

ICON_SIZE=64

DEFAULT_BG = "#1DB954"

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
        new_icon = PAUSE_ICON
        print("Playing")
    else:
        STATE = STATE_PAUSE
        new_icon = PLAY_ICON
        print("Pausing")
    
    button.configure(image=new_icon)
    button.photo = new_icon

def skip_song():
    print("Skipping to next song")

def previous_song():
    print("Going to previous song")

if __name__ == '__main__':
    STATE = STATE_PAUSE

    # Configure window
    root = tk.Tk()
    root.attributes('-type', 'dock')
    root.attributes('-fullscreen', True)
    root.geometry('480x320')
    root.configure(bg=DEFAULT_BG)
    root.focus_force()

    # Create all icons
    PLAY_ICON = tk.PhotoImage(file='res/play.png')
    PAUSE_ICON = tk.PhotoImage(file='res/pause.png')
    SKIP_ICON = tk.PhotoImage(file='res/skip.png')
    PREVIOUS_ICON = tk.PhotoImage(file='res/previous.png')

    # Create all fram,es
    album_art_frame = tk.Frame(master=root, width=256, height=256, bg="white")
    album_art_frame.place(x=(MAX_WIDTH-256)/2, y=0)

    play_pause_frame = tk.Frame(master=root, width=ICON_SIZE, height=ICON_SIZE, bg=DEFAULT_BG)
    play_pause_frame.place(x=(MAX_WIDTH/2)-(ICON_SIZE/2), y=MAX_HEIGHT-ICON_SIZE)

    skip_frame = tk.Frame(master=root, width=ICON_SIZE, height=ICON_SIZE, bg=DEFAULT_BG)
    skip_frame.place(x=(MAX_WIDTH/2)+2*(ICON_SIZE/2), y=MAX_HEIGHT-ICON_SIZE)

    previous_frame = tk.Frame(master=root, width=ICON_SIZE, height=ICON_SIZE, bg=DEFAULT_BG)
    previous_frame.place(x=(MAX_WIDTH/2)-(4*(ICON_SIZE/2)), y=MAX_HEIGHT-ICON_SIZE)

    # create all buttons
    play_pause = create_icon_button(PLAY_ICON, play_pause_frame)
    play_pause.configure(command= lambda: play(play_pause))

    skip = create_icon_button(SKIP_ICON, skip_frame)
    skip.configure(command=skip_song)

    previous = create_icon_button(PREVIOUS_ICON, previous_frame)
    previous.configure(command=previous_song)

    root.mainloop()