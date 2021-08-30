import tkinter
import os
from tkinter import *

window = Tk()
window.title("QRCode - by Zerbaib")
window.geometry("720x480")
window.minsize(480, 360)
window.iconbitmap("C:\Hugo\Python\qrcode\logo.ico")
window.config(background="#9EDBF8")
frame = Frame(window, bg="#9EDBF8")

label_title = Label(frame, text="Bienvenue sur QRCode", font=("Courrier", 40), bg="#9EDBF8", fg="white")
label_subtitle = Label(frame, text="QRCode est un logiciel qui permet de cree et de lire des QRCode", font=("Courrier", 25), bg="#9EDBF8", fg="white")
label_title.pack()
label_subtitle.pack()

cr_qr = Button(frame, text="Pour cree un qrcode click moi", font=("Courrier", 25), bg="white", fg="#9EDBF8")
re_qr = Button(frame, text="Pour lire un qrcode click moi", font=("Courrier", 25), bg="white", fg="#9EDBF8")
cr_qr.pack(pady=25, fill=X)
re_qr.pack(pady=25, fill=X)

# label_copy = Label(frame, text="2021 - 2021 | QRCodeByZerbaib © | Tout droit reserver", font=("Courrier", 15), bg="#9EDBF8", fg="white")
# label_copy.pack()

frame.pack(expand=YES)

window.mainloop()
input()