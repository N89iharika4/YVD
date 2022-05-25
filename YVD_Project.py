from tkinter import*
from tkinter import messagebox
from pytube import YouTube

root=Tk()
root.geometry('500x600')
root.title("Niharika-YouTube Video Downloader")

def Downloader():
    if link.get()=='':
        messagebox.showerror('Error','please enter the link')
    else:
        try:
            var.set("Downloading.....")
            YouTube(link.get()).streams.first().download()
            messagebox.showinfo('Complete','Video Downloaded Successfully')
            var.set('Paste the link below')
        except Exception:
            root.update()
            messagebox.showerror('Error','Invalid link,Please Enter the correct link')
            var.set('Enter the link below')
            link.set('')
            
var=StringVar()
link= StringVar()
var.set('Paste the Link Below:')

Label(root,text='YouTube Video Downloader',font='arial 20 bold',relief=RIDGE).pack()

link_enter=Entry(root,textvariable=var,font='arial 15',justify='center').pack()
link_enter2=Entry(root,textvariable=link,font='arial 15').pack()

    
Button(root,text='DOWNLOAD',font='arial 15 bold',bg='pale violet red',padx=2,command=Downloader).place(x=180,y=150)

root.mainloop()
