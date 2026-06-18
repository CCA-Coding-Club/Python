from tkinter import filedialog
from tkinter import *
import pygame
import os




root = Tk()
root.title("Music Player")
root.geometry("500x300") 

pygame.mixer.init() 


menubar = Menu(root)
root.config(menu=menubar) 

songs = []
current_song = ""
paused = False

def load_music():
    global current_song
    root.directory = filedialog.askdirectory() 
    
    if not root.directory:  # User cancelled
        return
        
    # Clear previous songs
    songs.clear()
    songlist.delete(0, END)
    
    for song in os.listdir(root.directory):
        name, ext = os.path.splitext(song)
        if ext == ".mp3":
            songs.append(song)
            
    for song in songs:
        songlist.insert("end", song)
    
    if songs:  # Only set selection if songs exist
        songlist.selection_set(0)
        current_song = songs[songlist.curselection()[0]]
    
def play_music():
    global current_song, paused
    
    if not songs:  # No songs loaded
        return
        
    if not paused:
        try:
            pygame.mixer.music.load(os.path.join(root.directory, current_song))
            pygame.mixer.music.play()
        except pygame.error:
            print(f"Could not play {current_song}")
    else:
        pygame.mixer.music.unpause()
        paused = False
    
    
def pause_music():
    global paused
    pygame.mixer.music.pause()
    paused = True

def next_music():
    global current_song, paused
    
    try:
        songlist.selection_clear(0, END)
        songlist.selection_set(songs.index(current_song) + 1)
        current_song = songs[songlist.curselection()[0]]
        play_music()
    except:
        pass
    
def prev_music():
    global current_song, paused
    
    try:
        songlist.selection_clear(0, END)
        songlist.selection_set(songs.index(current_song) - 1)
        current_song = songs[songlist.curselection()[0]]
        play_music()
    except:
        pass

organise_menu = Menu(menubar, tearoff = False)
organise_menu.add_command(label="Select Folder", command=load_music)
menubar.add_cascade(label="Organise", menu=organise_menu)


songlist = Listbox(root, bg = "black", fg = "white", width = 100, height = 15) 
songlist.pack() 

# Load images with error handling
try:
    play_btn_image = PhotoImage(file = "Images/play.png")  # Changed from Heart.png
    pause_btn_image = PhotoImage(file = "Images/pause.png") 
    next_btn_image = PhotoImage(file = "Images/next.png") 
    prev_btn_image = PhotoImage(file = "Images/previous.png")
except:
    # Fallback to text if images don't exist
    play_btn_image = None
    pause_btn_image = None
    next_btn_image = None
    prev_btn_image = None
    print("Warning: Could not load image files. Using text buttons.") 
control_frame = Frame(root) # Create a frame for control buttons
control_frame.pack() # Pack the control frame

# Create buttons with image or text fallback
if play_btn_image:
    play_btn = Button(control_frame, image = play_btn_image, borderwidth = 0, command=play_music)
else:
    play_btn = Button(control_frame, text="▶", borderwidth = 0, command=play_music)

if pause_btn_image:
    pause_btn = Button(control_frame, image = pause_btn_image, borderwidth = 0, command=pause_music)
else:
    pause_btn = Button(control_frame, text="⏸", borderwidth = 0, command=pause_music)

if next_btn_image:
    next_btn = Button(control_frame, image = next_btn_image, borderwidth = 0, command=next_music)
else:
    next_btn = Button(control_frame, text="⏭", borderwidth = 0, command=next_music)

if prev_btn_image:
    prev_btn = Button(control_frame, image = prev_btn_image, borderwidth = 0, command=prev_music)
else:
    prev_btn = Button(control_frame, text="⏮", borderwidth = 0, command=prev_music)

play_btn.grid(row = 0, column = 1, padx = 7, pady = 10) 
pause_btn.grid(row = 0, column = 2, padx = 7, pady = 10) 
next_btn.grid(row = 0, column = 3, padx = 7, pady = 10) 
prev_btn.grid(row = 0, column = 0, padx = 7, pady = 10) 

root.mainloop() 