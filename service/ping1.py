import tkinter
from tkinter import *
import ping3


def check(event=None):
    host = hostname.get()
    try:
        r = str(ping3.ping(host))
        ms = str(float(r) * 1000)
        msg = "    " + host + " : " + ms
        ping_answer.config(text=ms)
        label = Label(msg_list, text=msg, fg="#FF0000", bg="#000000")
        label.pack(side=TOP, fill=X)
    except:
        r = "    " + host + " : Error, please enter a valid ip address or hostname"
        ping_answer.config(text=r)


serv = Tk()

hostname = StringVar()

serv.title("check service status")
serv.configure(bg="#000000")

entry_field = tkinter.Entry(serv, textvariable=hostname, bg="#696969", fg="#FFFFFF")
ping_answer = Label(serv, text="service status", bg="#000000", fg="#FF0000")
host = Label(serv, textvariable=hostname, bg="#000000", fg="#FF0000")
scrollbar = tkinter.Scrollbar(serv)
msg_list = tkinter.Canvas(serv, yscrollcommand=scrollbar.set, bg="#000000")
send_button = tkinter.Button(serv, text="Check", command=check, bg="#000000", fg="#FF0000")


entry_field.bind("<Return>", check)
scrollbar.config(command=msg_list.yview)


host.pack(side=BOTTOM, fill=BOTH)
ping_answer.pack(side=BOTTOM, fill=BOTH)
send_button.pack(side=BOTTOM, fill=BOTH)
entry_field.pack(side=BOTTOM, fill=BOTH)
msg_list.pack(side=LEFT, fill=BOTH)
scrollbar.pack(side=RIGHT, fill=Y)

serv.mainloop()
