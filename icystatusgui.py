"""Tkinter GUI for icyStatus

Displays shoutcast streams in a nice GUI

"""
from Tkinter import *

def main():
    gui = icyStatusGui()



class icyStatusGui:
    def __init__(self):
        root = Tk()
        root.title("icyStatus - Currently Playing")
        win = Label(root, text="Hello") 
        win.pack()

        root.mainloop()





if __name__ == "__main__":
    main()