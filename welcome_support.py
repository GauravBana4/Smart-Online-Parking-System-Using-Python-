#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Feb 06, 2020 02:48:27 PM +0530  platform: Windows NT

import sys
from conn import conn
import easygui

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

def carpark(a,b,c,d):

    ct = conn()
    sql = "INSERT INTO carpark VALUES ('" + a + "', '" + b + "','" + c + "', '" + d + "')"
    ct.mycursor.execute(sql)
    ct.mydb.commit()

    # ---------------------------------------------------------------------

    sql = "UPDATE carsloat SET photo='1.JPG' WHERE IDd = '" + d + "'"
    ct.mycursor.execute(sql)
    ct.mydb.commit()

    # print(ct.mycursor.rowcount, "record Update ")
    a = easygui.msgbox("Record Update.", title="BOX")
    root.destroy()

    # ---------------------------------------------------------------------
    root.destroy()
   # import start
   # start.vp_start_gui()
    #sys.stdout.flush()

def viewcar():
    print("hh")
    import CarParking_new
    CarParking_new.parksloat()
    sys.stdout.flush()


def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    print("dd")
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import welcome
    welcome.vp_start_gui()




