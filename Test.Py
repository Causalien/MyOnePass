import Tkinter as tk

class SimpleApp(object):
    def __init__(self, master, **kwargs):
        title = kwargs.pop('title')
        frame = tk.Frame(master, borderwidth=5, bg = 'cyan', **kwargs)
        frame.grid()
        button = tk.Button(frame, text = title)
        button.grid(sticky = tk.SE)
        frame.rowconfigure('all', minsize = 200)
        frame.columnconfigure('all', minsize = 200)

def basic():
    root = tk.Tk()
    app = SimpleApp(root, title = 'Hello, world')
    root.mainloop()
basic()