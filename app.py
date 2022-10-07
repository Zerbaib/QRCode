 # # # Modules
#
import sys
import os
import tkinter
from tkinter import *
#
 # # # Fin des modules

 # # # Commands
#
def CreateQRCode():
    os.system('create_qrcode.py')
def ReadQRCode():
    os.system('read_qrcode.py')
#
 # # # Fin des commands

 # # # Onglet
#
window = Tk()
window.title("QRCode - by Zerbaib")
window.geometry("720x480")
window.minsize(480, 360)
window.iconbitmap("logo.ico")
window.config(background="#9EDBF8")
frame = Frame(window, bg="#9EDBF8")
#
 # # # Fin de l'onglet

 # # # Text
#
label_title = Label(frame, text="Bienvenue sur QRCode", font=("Courrier", 40), bg="#9EDBF8", fg="white")
label_subtitle = Label(frame, text="QRCode est un logiciel qui permet de cree et de lire des QRCode", font=("Courrier", 25), bg="#9EDBF8", fg="white")
label_title.pack()
label_subtitle.pack()
#
 # # # Fin du text

 # # # Boutons
#
cr_qr = Button(frame, text="Pour cree un qrcode click moi", font=("Courrier", 25), bg="white", fg="#9EDBF8",command= CreateQRCode)
re_qr = Button(frame, text="Pour lire un qrcode click moi", font=("Courrier", 25), bg="white", fg="#9EDBF8",command= ReadQRCode)
cr_qr.pack(pady=20, fill=X)
re_qr.pack(pady=20, fill=X)
#
 # # # Fin des bontons

frame.pack(expand=YES)

window.mainloop()
input()
