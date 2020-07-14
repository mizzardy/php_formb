from source import *
from tkinter import *


class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()

        self.get_url = Entry()
        self.get_url.pack()
        self.send_brute = Button(command=self.accept_url,text="Go!")
        self.send_brute.pack()
        self.send_brute.bind("1", self.accept_url)


    def accept_url(self):
        self.password = self.get_url.get()
        brute_url(self.password)
        generate_login("data.txt")
        post_data()

new_app = App()
new_app.master.title("brute-force")
new_app.master.minsize(250, 50)
new_app.master.resizable(width=False, height=False)
new_app.mainloop()
