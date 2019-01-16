from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict
from youtube_dl import YoutubeDL

url = "https://www.apple.com/itunes/charts/songs/"
conn = urlopen(url)
raw_data = conn.read()
content = raw_data.decode("utf8")

soup = BeautifulSoup(content, "html.parser")
songs = soup.find("ul", "")

li_list = songs.find_all("li")

songs_list = []

for li in li_list:
    h3 = li.h3
    h4 = li.h4
    name = h3.string
    artist = h4.string
    song = OrderedDict({
        "name": name,
        "artist": artist,
    })
    songs_list.append(song)

    options = {
        "default_search": "ytsearch",
        "max_download": 1,
        "format": "bestaudio/audio"
    }
    dl = YoutubeDL(options)
    dl.download([name + " " + artist])

pyexcel.save_as(records=songs_list, dest_file_name="itunes_chart.xls")

