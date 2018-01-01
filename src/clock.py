#!/usr/bin/env python3
# -*- coding: utf_8 -*-
"""

    Copyright    : 2018 January. A. R. Bhatt.
    Organization : VAU SoftTech
    Project      : gui-clock - Simple gui clock using python and tkinter
    Script Name  : header-template.py
    License      : GNU General Public License v3.0


    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""
try:
    import Tkinter as tk
    import Tkinter.messagebox
except:
    from tkinter import *
    from tkinter import messagebox

from datetime import datetime as dttm

class Clock(Frame):

    def __init__(self,parent=None):
        Frame.__init__(self, parent)
        self.master = parent
        scr_width =  parent.winfo_screenwidth()
        scr_height = parent.winfo_screenheight()
        app_width = 700
        app_height = 150
        x_pos = int( (scr_width - app_width) / 2 )
        y_pos = int( (scr_height - app_height) / 2 )
        self.master.geometry(f"{app_width}x{app_height}+{x_pos}+{y_pos}")
        self.master.title("VAU - Clock")
        self.master.protocol("WM_DELETE_WINDOW", self.client_exit)
        self.master.resizable(False, False)
        self.pack(fill=BOTH, expand=1)
        self.make_widgets()
        photo = PhotoImage(file = 'logo.png')
        self.master.iconphoto(False, photo)

    def make_widgets(self):
        menu = Menu(self.master)
        self.master.config(menu=menu)
        fl = Menu(menu)
        fl.add_command(label=" Exit ", command=self.client_exit)
        menu.add_cascade(label=" File ", menu=fl)

        self.label = Label(self, text ="Clock", width=100, fg="red")
        self.label.configure(font=("Ubuntu Light", 34))
        self.label.after(500, self.update_label)
        self.label.pack()

    def client_exit(self):
        if messagebox.askquestion("Decide", "Are you sure to exit?") == 'yes':
           self.master.destroy()
        else:
           messagebox.showinfo('Return','OK then, you will now return to the application screen')

    def update_label(self):
        self.label.configure(text="{:%A %B %d, %Y\n%X}".format(dttm.now()))
        self.master.update()
        self.label.after(500, self.update_label)

main = Tk()
app = Clock(main)
app.mainloop()
