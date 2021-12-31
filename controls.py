import tkinter as tk
import os
import subprocess

os.system('rhythmbox-client --pause')

window = tk.Tk()
window.wait_visibility(window)
window.wm_attributes('-alpha',0.8)
window.title(string='Rhythmbox Controls')
window.attributes('-topmost', True)
hs = window.winfo_screenheight()
h, w = 50, 340
x, y = 0, hs-h
window.geometry('%dx%d+%d+%d' % (w, h, x, y))


playing = subprocess.getoutput('rhythmbox-client --print-playing')

#find images
pauseimage = tk.PhotoImage(file='~/.rhythmboxcontrols/pause.gif')
nextimage = tk.PhotoImage(file='~/.rhythmboxcontrols/next.gif')
previousimage = tk.PhotoImage(file='~/.rhythmboxcontrols/previous.gif')
playimage = tk.PhotoImage(file='~/.rhythmboxcontrols/play.gif')
playpauselist = [pauseimage, playimage]
playpauseindex = 0

#create things
song = tk.Label(window, text=playing)
playpause = tk.Button(window, image = playimage, width=20, height=20)
next = tk.Button(window, image = nextimage, width=20, height=20)
previous = tk.Button(window, image = previousimage, width=20, height=20)


#define buttons
def playpausepress(event):
    global playpauseindex
    os.system('rhythmbox-client --play-pause')
    if playpauseindex > 1:
        playpauseindex = 0
    playpause.config(image = playpauselist[playpauseindex])
    playpauseindex += 1
def nextpress(event):
    os.system('rhythmbox-client --next')
    playing = subprocess.getoutput('rhythmbox-client --print-playing')
    song.config(text=playing)
def previouspress(event):
    os.system('rhythmbox-client --previous')
    playing = subprocess.getoutput('rhythmbox-client --print-playing')
    song.config(text=playing)
def updatesongname():
    window.after(1000, updatesongname)
    playing = subprocess.getoutput('rhythmbox-client --print-playing')
    song.config(text=playing)



updatesongname()

#bind buttons
playpause.bind('<Button-1>', playpausepress)
next.bind('<Button-1>', nextpress)
previous.bind('<Button-1>', previouspress)


#position everything
next.place(x=190, y=20)
playpause.place(x=160, y=20)
previous.place(x=130, y=20)
song.place(x=0, y=0)


window.mainloop()
