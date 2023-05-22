from customtkinter import *
from customtkinter import filedialog
from CTkMessagebox import CTkMessagebox
from downloader import FILEtd


root = CTk()
root.title("Youtube Video Downloader")
root.resizable(False, False)
root.geometry('500x200')
url_box = CTkTextbox(root, height=1, width=500)
url_box.grid(row=0, column=0, columnspan=3)
loc = StringVar()
display_loc = CTkLabel(root, textvariable=loc)
folder_selected = " "


def on_browse():
    global folder_selected
    folder_selected = filedialog.askdirectory()
    loc.set("Download At\t"+folder_selected)


def download():
    url = url_box.get('1.0', "end-1c")
    if len(url.replace(" ", "")) == 0:
        CTkMessagebox(title="Error", message="URL missing", icon="cancel")

    elif len(folder_selected.replace(" ", "")) == 0:
        CTkMessagebox(title="Error", message="Download Location Missing", icon="cancel")

    else:
        print(folder_selected, url)
        video = FILEtd(url=url, location=folder_selected)
        try:
            video.dwnld()

        except Exception as e:
            CTkMessagebox(title="Error", message="Invalid URL", icon="cancel")
            print(e)


if __name__ == '__main__':
    browse_button = CTkButton(root, text="Browse", command=on_browse)
    download_button = CTkButton(root, text="Download", command=download)
    display_loc.grid(row=2, column=0, columnspan=3)
    browse_button.grid(row=4, column=0)
    download_button.grid(row=4, column=2)
    root.mainloop()


