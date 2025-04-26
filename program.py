# Coder: 0silat0r
# Date: 18.05.2024

import tkinter
import pytube
from pytube import YouTube
from tkinter import *
from PIL import Image, ImageTk

def video_download():
    print("Lütfen bekleyin kurulum başlatılıyor...")
    link = t1.get(1.0,"end-1c")
    path = "Downloads/"
    pytube.YouTube(link).streams.get_highest_resolution().download(path)
    print("Video Indirildi!")
    print("Indirdiginiz videoyu Downloads klasöründe bulabilirsiniz.")
    t1.delete("1.0","end")

program = tkinter.Tk()
program.geometry('385x280')
program.title("YouTube Video Downloader")

img = Image.open("pictures/youtube-logo.png")
resize_img = img.resize((165,140))
img2 = ImageTk.PhotoImage(resize_img)
img_lbl = Label(image=img2)
img_lbl.image = img2
img_lbl.pack()

l1 = Label(program, text="Video Source Link")
l1.pack()

t1 = Text(program, width=42,height=1)
t1.pack()
t1.option_clear()

b1 = Button(program, text="Video Download",command=video_download)
b1.pack()
b2 = Button(program, text="Quit",command=program.destroy)
b2.pack()

l2 = Label(program, text='Programming by 0silat0r')
l2.pack()

program.mainloop()
