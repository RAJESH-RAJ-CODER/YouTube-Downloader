from pytube import *
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from threading import *
import tkinter
import os

# Total Size Container..............................

file_size = 0


# This Function is For Updating Percentage...............

#def progress(stream=None, chunk=None, file_handle=None, remaining=None):
    # pass

    # Gets The Percentage of The File That Has Been Downloaded...............

    #file_downloaded = (file_size - remaining)
   # per = (file_downloaded / file_size) * 100

    #dBtn.config(text="{}%downloaded".format(per))


# Starting to Downloading Video.........................

def startDownload():
    global file_size
    try:
        url = urlField.get()
        print(url)

        # Changing Button Test.................................

        dBtn.config(text="Please Wait.....")
        dBtn.config(state=DISABLED)
        path_to_save_video = askdirectory()
        print(path_to_save_video)
        if path_to_save_video is None:
            return

        # Creating YouTube Object with Url..................

        ob = YouTube(url)#,on_progress_callback=progress)
        strm = ob.streams.first()
        #print(strm)
        file_size = strm.filesize
        vTitle.config(text=strm.title)
        vTitle.pack(side=TOP)
        print(file_size)
        strm.download( path_to_save_video)
        #strm.download(path_to_save_video)
        print("Done......")
        dBtn.config(text="start Download")
        dBtn.config(state=NORMAL)
        showinfo("Download Finished", "Download Successfully")
        urlField.deleted(0, END)
        vTitle.pack_forget()

    except Exception as e:
        print(e)
        print("Error..!")


def startDownloadThread():
    # Create a Thread...........

    thread = Thread(target=startDownload)
    thread.start()


# Starting Gui Building............................

main = tkinter.Tk()
# Setting The Title.................

main.title("My YouTube Downloader")

# Set The Icon

#main.iconbitmap('icon.ioc')

# Set Screen Size..........
main.geometry('900x450')
#main.geometry("700X700")

# set Heading Icon And First Declare File Variable.......

file = PhotoImage(file="youtube.png")

headingIcon = Label(main, image=file)
headingIcon.pack(side=TOP)

# Url TextField Setting....................................
urlField = Entry(main, font=("vardana", 18), justify=CENTER)
urlField.pack(side=TOP, fill=X, padx=10)
# Download Button Creation........................
dBtn = Button(main, text="start download", font=("vardana", 18), relief="ridge", command=startDownloadThread)
dBtn.pack(side=TOP,pady=10)

# video Title..........................

vTitle = Label(main, text="video title")
# Ending of the Main Loop With Gui Development.............................
lbl6=Label(main,text='©Rajesh Raj', width='130',fg='black',bg='cyan',font=('times',13,'bold'))
lbl6.pack(side=BOTTOM)

main.mainloop()
