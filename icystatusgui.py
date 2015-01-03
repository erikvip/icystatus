"""Tkinter GUI for icyStatus

Displays shoutcast streams in a nice GUI

"""
from Tkinter import *
import ttk

from icystatus import fetchStatus
from subprocess import Popen
import os
import pprint

def main():
    gui = icyStatusGui()



class icyStatusGui:

    def __init__(self):
        self.root = Tk()
        self.root.title("icyStatus - Currently Playing")

        self.root.geometry("900x600+100+100")
        #self.root.config(menu=self.menubar)
        img = PhotoImage(file='images/shoutcast.png')
        self.root.tk.call('wm', 'iconphoto', self.root._w, img)

        '''
        style = ttk.Style()
        style.configure("BW.TLabel", foreground="black", background="white")        
        self.menubar = Menu(self.root)
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Quit", command=self.root.quit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        '''

        
        # Main Toolbar
        toolbar = Frame(self.root, bd=1, relief=RAISED)
        self.refreshButtonImage = PhotoImage(file=os.path.realpath("images/arrow_refresh.png"))

        self.refreshButton = Button(toolbar, 
                                text="Refresh", 
                                image=self.refreshButtonImage, 
                                compound=LEFT, 
                                relief=FLAT,
                                command=self.refreshAll
                        ).pack(side=LEFT)

        toolbar.pack(side=TOP, fill=X)

        self.grid = Frame(self.root, bd=1)
        self.grid.pack(fill=BOTH, expand=1)


        self.status = StringVar()
        self.statusFrame = Frame(self.root, bd=1, relief=RAISED)
        self.statusLabel = Label(self.statusFrame, textvariable=self.status, anchor=W, justify=LEFT).pack(fill=X, expand=1)
        self.statusFrame.pack(side=BOTTOM, fill=X)

        # Main listbox 
        Label(self.grid, text="Station", width = 10, font="Verdana 10 bold").grid(row = 0, column = 0)
        Label(self.grid, text="URL", width = 10, font="Verdana 10 bold").grid(row = 0, column = 1)
        Label(self.grid, text="Current Track", width = 30, font="Verdana 10 bold").grid(row = 0, column = 2)

        #self.icyStatus()
        self.refreshAll()


        self.root.mainloop()

       
    def refreshAll(self):
        '''Refresh all streams'''
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

        self.rowCounter = 1
        for url in urls:
            self.icyStatus(url)

        self.status.set("Refresh complete")
        self.root.update_idletasks()


    def icyStatus(self, url):
        
        self.status.set("Refreshing {0} ...".format(url))
        self.root.update_idletasks()
        
        stats = fetchStatus([url])
      
        r = self.rowCounter

        for i in stats:

#            self.status.set("Refreshing {0}...".format(i['StreamUrl'] ))
#            self.root.update_idletasks()

            Label(self.grid, text=i['Name'][:30], bg="#EEEEEE").grid(row = r, column=0, sticky="w", padx=5, pady=1)
            Label(self.grid, text=i['StreamUrl'][:30]).grid(row = r, column=1, sticky="w", padx=5, pady=1)
            Label(self.grid, text=i['CurrentTrack'][:30]).grid(row = r, column=2, sticky="w")

            Button(self.grid, text="Launch", command=lambda u=i['LaunchUrl']: self.launchStream(u)).grid(row = r, column=3)

            r = r + 1;
            self.rowCounter = r



    def launchStream(self, url):
        '''Launch stream in external player'''
        Popen(['/usr/bin/vlc', url])



if __name__ == "__main__":
    main()