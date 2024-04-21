import os
from tkinter import *
import webview
import shutil
import webbrowser
from PIL import Image,ImageTk
from tkinter.messagebox import showerror,showinfo
from tkinter.filedialog import askopenfile

class data:
    creator = 'Pavan'
    geometry = '400x200'
    app_name = 'PDF Reader'

def open_pdf():
    file=askopenfile()
    page_code = ""
    with open('boiler.txt') as boiler:
        for i in boiler.readlines():page_code+=f"{i}\n"
    if 'file.pdf' in os.listdir():
        os.remove('file.pdf')
    shutil.copyfile(file.name,'file.pdf')
    obj = f"""<object class="pdf" 
            data="file.pdf" 
            width="800" height="500"></object></body></html>"""
    page_code+=obj
    with open('page.html','w+') as pge:
        pge.write(page_code)
    webview.create_window('PdfReader.py','page.html') 
    webview.start() 

def about_me():
    showinfo('About','A pdf reader written in python language.')

def github_link():
    webbrowser.open('https://github.com/pavkcodes')

def yt_link():
    webbrowser.open('https://outube.com/@pavkcodes')

def mail_me():
    showinfo('Mail to :','pavan.mailforuse@gmail.com')

if __name__=='__main__':
    
    app = Tk()

    app.title(data.app_name)
    app.geometry(data.geometry)
    # app.iconbitmap('icon.ico')
    
    menuBar = Menu(app)
    
    fileMenu = Menu(menuBar,tearoff=0)
    menuBar.add_cascade(label='File', menu=fileMenu)
    fileMenu.add_command(label='Open',command=open_pdf)
    fileMenu.add_separator()
    fileMenu.add_command(label='Exit',command=app.quit)
    
    aboutMenu = Menu(menuBar,tearoff=0)
    menuBar.add_cascade(label='About', menu=aboutMenu)
    aboutMenu.add_command(label='About Me',command=about_me)
    aboutMenu.add_command(label='Github Link',command=github_link)
    aboutMenu.add_command(label='Youtube Link',command=yt_link)

    contactMenu = Menu(menuBar,tearoff=0)
    menuBar.add_cascade(label='Contact', menu=contactMenu)
    contactMenu.add_command(label='Email',command=mail_me)

    app.config(menu=menuBar)
    
    Label(app,text="Name   :").grid(row=1,column=1,sticky=W)
    Label(app,text="PDF Reader").grid(row=1,column=2,sticky=W)

    Label(app,text="Desc   :").grid(row=2,column=1,sticky=W)
    Label(app,text="a pdf reading program written in python3 \n just to view pdf file and doddle.").grid(row=2,column=2,sticky=W)

    Label(app,text="Made by:").grid(row=3,column=1,sticky=W)
    Label(app,text="Pavan Kumar").grid(row=3,column=2,sticky=W)

    app.mainloop()