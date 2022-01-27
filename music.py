import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os

musicplayer = tkr.Tk()
musicplayer.title("Music Player")      #Title
musicplayer.geometry("450x350")        #Set size of window

directory = askdirectory()
os.chdir(directory)                     #Used to change current working directory to specified path
songlist = os.listdir()                 #Returns the list containing the names of entries in directory given by path
playlist = tkr.Listbox(musicplayer, font ="Helvetica 12 bold", bg="yellow",selectmode= tkr.SINGLE)   #Used to display list items to the user

for item in songlist:
    pos = 0
    playlist.insert(pos, item)
    pos = pos + 1

pygame.init()
pygame.mixer.init()                      # Module used for loading and playing sound

def play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))   #Module for controlling streamed audio and also loads  a music file for playback
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()

def ExitMusicPlayer():
    pygame.mixer.music.stop()

def pause():
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()

Button1 = tkr.Button(musicplayer,width=5,height=3, font="Helvetica 12 bold",text="PLAY",command=play,bg="red",fg="white")
Button2 = tkr.Button(musicplayer,width=5,height=3, font="Helvetica 12 bold",text="STOP",command=ExitMusicPlayer,bg="purple",fg="white")
Button3 = tkr.Button(musicplayer,width=5,height=3, font="Helvetica 12 bold",text="PAUSE",command=pause,bg="green",fg="white")
Button4 = tkr.Button(musicplayer,width=5,height=3, font="Helvetica 12 bold",text="UNPAUSE",command=unpause,bg="blue",fg="white")


var = tkr.StringVar()            # StringVar() is a class from tkinter used to monitor changes to take into variables
songtitle = tkr.Label(musicplayer, font="Helvetica 12 bold", textvariable=var)

songtitle.pack()           #pack() just arrange song title inside the application window on the next widget
Button1.pack(fill="x")
Button2.pack(fill="x")
Button3.pack(fill="x")
Button4.pack(fill="x")
playlist.pack(fill="both",expand="yes")

musicplayer.mainloop()
