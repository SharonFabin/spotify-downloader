import spotdl
import clipboard
from shutil import copyfile
from os import listdir, remove
from os.path import isfile, join
from pathlib import Path
import ctypes

path = "C:/Users/User/OneDrive/Music"


def download(url: str):
    try:
        ans = ctypes.windll.user32.MessageBoxW(0, f"Start downloading this URL?\n\n{url}?", "Success", 1)
        if ans == 1:
            if not (url.startswith("https://open.spotify.com") or url.startswith("https://youtu.be")):
                raise Exception("Bad URL!")
            downloader = spotdl.Spotdl()
            downloader.download_track(url)
            song_files = [f for f in listdir("./") if isfile(join("./", f)) and f != "main.py"]
            copyfile(f"./{song_files[0]}", f"{path}/{song_files[0]}")
            remove(song_files[0])
            ctypes.windll.user32.MessageBoxW(0, f"Done downloading {song_files[0]}", "Success", 0)
    except Exception as e:
        ctypes.windll.user32.MessageBoxW(0, str(e), "Fail", 0)


if __name__ == '__main__':
    download(clipboard.paste())
