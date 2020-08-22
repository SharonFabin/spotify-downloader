import spotdl
import clipboard
import enchant
from shutil import copyfile
from os import listdir, remove, mkdir
from os.path import isfile, join
from pathlib import Path, PurePath
import ctypes

path = Path(Path.home(), "Desktop/Music")


def download(url: str):
    try:
        ans = ctypes.windll.user32.MessageBoxW(0, f"Start downloading this URL?\n\n{url}", "Success", 1)
        if ans == 1:
            dict = enchant.Dict("en_US")
            words = url.split(' ', 1)
            if not dict.check(words[0]) and not (url.startswith("https://open.spotify.com") or url.startswith("https://youtu.be")):
                raise Exception("Bad URL!")
            downloader = spotdl.Spotdl()
            downloader.download_track(url)
            default_files = ["main.py", "setup.cmd", "song-download.cmd", ".gitignore"]
            song_files = [f for f in listdir("./") if isfile(join("./", f)) and f not in default_files]
            if not path.exists():
                path.mkdir()
            copyfile(f"./{song_files[0]}", Path(path, song_files[0]))
            remove(song_files[0])
            ctypes.windll.user32.MessageBoxW(0, f"Done downloading {song_files[0]}", "Success", 0)
    except Exception as e:
        ctypes.windll.user32.MessageBoxW(0, str(e), "Fail", 0)


if __name__ == '__main__':
    download(clipboard.paste())
