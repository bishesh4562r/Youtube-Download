from youtube_dl import YoutubeDL
from CTkMessagebox import CTkMessagebox

class FILEtd:
    def __init__(self, url, location):
        self.url = url
        self.location = location

    def dwnld(self):
        ydl_opts = {
            'outtmpl': f'{self.location}/%(extractor_key)s/%(extractor)s-%(id)s-%(title)s.%(ext)s',

        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([self.url])
            CTkMessagebox(title="video downloaded", message="download successful")


