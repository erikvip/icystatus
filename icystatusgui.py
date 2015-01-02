"""Tkinter GUI for icyStatus

Displays shoutcast streams in a nice GUI

"""
from Tkinter import *
from icystatus import fetchStatus
import pprint

def main():
    gui = icyStatusGui()



class icyStatusGui:



    def __init__(self):
        self.root = Tk()
        self.root.title("icyStatus - Currently Playing")
        #self.root.maxsize(800,600)

#        self.win = Label(self.root, text="Hello", width=200, height=75) 
 #       self.win.pack()




        # Main listbox 
        #self.listbox = Listbox(self.root)
        #self.listbox.pack()
        Label(self.root, text="Station", width = 10).grid(row = 0, column = 0)
        Label(self.root, text="URL", width = 10).grid(row = 0, column = 1)
        Label(self.root, text="Current Track", width = 30).grid(row = 0, column = 2)

        self.icyStatus()

        self.root.mainloop()

        

    def icyStatus(self):


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
        ]

        stats = fetchStatus(urls)
        pprint.pprint(stats)

        r = 1
        for i in stats:
            Label(self.root, text=i['Name'][:20]).grid(row = r, column=0)
            Label(self.root, text=i['StreamUrl']).grid(row = r, column=1)
            Label(self.root, text=i['CurrentTrack']).grid(row = r, column=2)

            r = r + 1;







if __name__ == "__main__":
    main()