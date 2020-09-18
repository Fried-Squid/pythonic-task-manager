import win32con
import win32api
import win32security
import importlib.util
import tkinter as tk
from tkinter import ttk
spec = importlib.util.spec_from_file_location("module.wmi", "E:\\!CompSci\\taskmanager_py\\Proc-Monitor\\" + "/build/lib/wmi.py")
wmi = importlib.util.module_from_spec(spec)
spec.loader.exec_module(wmi)
import sys
import os
from threading import Thread
from re import *
from datetime import date
import subprocess

#VARIABLES
CREATE_NO_WINDOW = 0x08000000
# DEFINES
def start():
     subprocess.call("c:\\windows\\system32\\rundll32.exe shell32.dll,#61", creationflags=CREATE_NO_WINDOW)
def end():
     subprocess.call("taskkill /F /PID " + str(proc_display.item(proc_display.selection())['values'][2]), creationflags=CREATE_NO_WINDOW)
     update()
def update():
     v1.set("UPDATING")
     mainthread()
     print("UPDATING")
     v1.set("IDLE")
global colors
colors = ["white", "black", "red", "green", "blue", "cyan", "yellow", "magenta", "grey"]
colorsiter = iter(colors)

# INSTANCES
c = wmi.WMI()


#TK SETUP
root = tk.Tk()
root.title("Task Manager")
#content = tk.Frame(root)
#content.grid(column=24, row=12, sticky="N S E W")
for i in range(1,12):
     root.columnconfigure(i,weight=1)
for i in range(1,24):
     root.rowconfigure(i,weight=1)
proc_display = ttk.Treeview(root)
proc_display.grid(row=0, column=0, rowspan=12, columnspan=24)

b1 = tk.Button(root, text="Start Task", command=start)
b2 = tk.Button(root, text="Edit Task",  command=start)
b3 = tk.Button(root, text="End Task",   command=end  )
b4 = tk.Button(root, text="Options",    command=start)
b5 = tk.Button(root, text="Update",     command=update)
b6 = tk.Button(root, text="Placeholder",command=start)
b7 = tk.Button(root, text="Placeholder",command=start)
b8 = tk.Button(root, text="Placeholder",command=start)
v1 = tk.StringVar()
v1.set("INITALISING")
l1 = tk.Label(root, textvariable=v1)
l1.grid(column=24,row = 10, sticky = "S W", columnspan=2 )
b1.grid(column=24, row = 1, sticky = "W E", columnspan=2 )
b2.grid(column=24, row = 2, sticky = "W E", columnspan=2 )
b3.grid(column=24, row = 3, sticky = "W E", columnspan=2 )
b4.grid(column=24, row = 4, sticky = "W E", columnspan=2 )
b5.grid(column=24, row = 5, sticky = "W E", columnspan=2 )
b6.grid(column=24, row = 6, sticky = "W E", columnspan=2 )
b7.grid(column=24, row = 7, sticky = "W E", columnspan=2 )
b8.grid(column=24, row = 8, sticky = "W E", columnspan=2 )

proc_display["columns"] = ("NAME", "CMDLINE", "PID", "PARENT PID", "PRIVELEGES")
proc_display.heading("#0", text="TIME")
proc_display.heading("NAME", text="NAME")
proc_display.heading("CMDLINE", text="CMDLINE")
proc_display.heading("PID", text="PID")
proc_display.heading("PARENT PID", text="PARENT PID")
proc_display.heading("PRIVELEGES", text="PRIVELEGES")

proc_display.column('#0', width=100, anchor='center')
proc_display.column('NAME', width=150, anchor='center')
proc_display.column('CMDLINE', width=200, anchor='center')
proc_display.column('PID', width=50, anchor='center')
proc_display.column('PARENT PID', width=75, anchor='center')
proc_display.column('PRIVELEGES', width=100, anchor='center')

def mainthread():
     proc_display.delete(*proc_display.get_children())
     for process in c.Win32_process():
          try:
              t = None
              privileges  = "N/A"
              proc_owner  = process.name
              create_date = process.CreationDate
              executable  = process.ExecutablePath
              cmdline     = process.CommandLine
              pid         = str(process.ProcessId)
              parent_pid  = str(process.ParentProcessId)
              y           = create_date[:2] + '/' + create_date[2:]
              y           = y[:5] + '/' + y[5:]
                   
              t = [str(y[:8]), str(proc_owner), str(cmdline).strip("//").strip('"'), str(pid), str(parent_pid), str(privileges)]
          except Exception as e:
               t = None
               print(e)
          if t != None:
               proc_display.insert("", "end", text=str(t[0]),values=(t[1],t[2],t[3],t[4],t[5]))
          else:
               pass
while True:
     root.update_idletasks()
     root.update()

