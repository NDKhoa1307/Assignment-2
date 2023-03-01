#
#  Numbering conversion system with external UI
#  Status: On-going
#

import tkinter as tk

if __name__ == '__main__':
    win = tk.Tk()
    lbl = tk.Label(win, text = "Python rocks!")
    lbl.pack()

    entry = tk.Entry(fg="black", bg="white", width=50)
    entry.pack()
    
    win.mainloop()