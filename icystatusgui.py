"""Tkinter GUI for icyStatus

Displays shoutcast streams in a nice GUI

"""
from Tkinter import *
import ttk

from icystatus import fetchStatus
import pprint

def main():
    gui = icyStatusGui()



class icyStatusGui:



    def __init__(self):
        self.root = Tk()
        self.root.title("icyStatus - Currently Playing")
        #self.root.maxsize(800,600)

        '''
        style = ttk.Style()
        style.configure("BW.TLabel", foreground="black", background="white")        
        self.menubar = Menu(self.root)
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Quit", command=self.root.quit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        '''

        
        toolbar = Frame(self.root, bd=1, relief=RAISED)
        refreshButton = Button(toolbar, text="Refresh", relief=FLAT, command=self.icyStatus).pack(side=LEFT)
        toolbar.pack(side=TOP, fill=X)

        self.grid = Frame(self.root, bd=1)
        self.grid.pack(fill=BOTH, expand=1)


        self.status = StringVar()
        self.statusFrame = Frame(self.root, bd=1, relief=RAISED)
        self.statusLabel = Label(self.statusFrame, textvariable=self.status, anchor=W, justify=LEFT).pack(fill=X, expand=1)
        self.statusFrame.pack(side=BOTTOM, fill=X)

        # Main listbox 
        Label(self.grid, text="Station", width = 10).grid(row = 0, column = 0)
        Label(self.grid, text="URL", width = 10).grid(row = 0, column = 1)
        Label(self.grid, text="Current Track", width = 30).grid(row = 0, column = 2)

        self.icyStatus()

        self.root.geometry("800x450+300+300")
        #self.root.config(menu=self.menubar)

        self.root.mainloop()

        

    def icyStatus(self):
        
        self.status.set("Refreshing...")

        # SomaFM URLs
        urls = [
            'http://xstream1.somafm.com:8062',
            'http://xstream1.somafm.com:2800',
            'http://xstream1.somafm.com:8900',
            'http://uwstream2.somafm.com:80',
            'http://uwstream2.somafm.com:8400',
            'http://uwstream1.somafm.com:80',
            'http://xstream1.somafm.com:8800',
            'http://xstream1.somafm.com:2020',
            'http://xstream1.somafm.com:2200',
            'http://uwstream3.somafm.com:8000',
            'http://xstream1.somafm.com:2504',
            'http://xstream1.somafm.com:8884',
            'http://uwstream2.somafm.com:7770',
            'http://205.164.62.15:6900',
            'http://108.61.73.115:8052',
            'http://listen.radionomy.com/AdultAlternative',

        ]
        '''
        urls = [
        'http://205.164.62.15:6900',
        'http://108.61.73.115:8052',
        'http://listen.radionomy.com/AdultAlternative'
        ]
        '''

        stats = fetchStatus(urls)
      
        r = 1
        for i in stats:
            Label(self.grid, text=i['Name'][:20], bg="#EEEEEE", anchor=W, justify=LEFT).grid(row = r, column=0)
            Label(self.grid, text=i['StreamUrl'][:30]).grid(row = r, column=1)
            Label(self.grid, text=i['CurrentTrack']).grid(row = r, column=2)

            r = r + 1;

        self.status.set("Refresh complete")


if __name__ == "__main__":
    main()