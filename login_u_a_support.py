#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Feb 13, 2020 03:16:48 PM +0530  platform: Windows NT

import sys
import easygui
from conn import conn

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk

    py3 = False
except ImportError:
    import tkinter.ttk as ttk

    py3 = True


def set_Tk_var():
    global combobox
    combobox = tk.StringVar()


def log(a, b):
    ct1 = 0
    ct = conn()

    ct.mycursor.execute("SELECT * FROM reg where user_nm='" + a + "' and   password='" + b + "'")
    myresult = ct.mycursor.fetchall()

    for x in myresult:
        ct1 = ct1 + 1

    if (ct1 > 0):
        print(ct1)
        easygui.msgbox("Login Sucessfully ", title="BOX")
        root.destroy()
        import welcome
        welcome.vp_start_gui()




def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top


def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None


if __name__ == '__main__':
    import login_u_a

    login_u_a.vp_start_gui()