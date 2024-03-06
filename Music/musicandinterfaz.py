from pytube import YouTube 
import os 
from tkinter import *
from tkinter import ttk

def accion():
    enlace = enlaceinput.get()
    destinoalmacenamiento = direccion.get()
    print("Sacando audio del enlace: " + enlace)

    yt=YouTube(enlace)
    print(yt.title + " is downloading")

    audio = yt.streams.filter(only_audio=True).first() 

    out_file = audio.download(output_path=destinoalmacenamiento)

    base, ext = os.path.splitext(out_file) 
    new_file = base + '.mp3'
    os.rename(out_file, new_file) 

    print(yt.title + " has been successfully downloaded.")




root = Tk()
root.config(bd=25)
root.title("Scrip para descargar audios de videos")
imagen = PhotoImage(file = "Music/imagenes/ytlogo.png")
foto = Label(root, image=imagen, bd=0)
foto.grid(row=0, column=0)
frm = ttk.Frame(root)
frm.grid()
ttk.Label(frm, text="App de descargas").grid(column=0, row=0)


instrucciones = Label(root, text="pegar un link de YT para descargar")
instrucciones.grid (row=2,column=2)

enlaceinput = Entry(root)
enlaceinput.grid(row=2,column=3)

destino = Label(root, text="pegar el lugar de almacenamiento")
destino.grid (row=3,column=2)

direccion = Entry(root)
direccion.grid(row=3,column=3)

ttk.Button(frm, text="Descargar", command=accion).grid(column=1, row=4)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=4)
root.mainloop()


