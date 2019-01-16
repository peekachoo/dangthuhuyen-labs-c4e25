from youtube_dl import YoutubeDL

# 1. Download a single youtube video:
dl = YoutubeDL()
dl.download(["https://www.youtube.com/watch?v=KUWvIftDc4k"])

# 2. Download multiple youtueb videos:
dl = YoutubeDL()
dl.download(["https://www.youtube.com/watch?v=q6EoRBvdVPQ", "https://www.youtube.com/watch?v=kMoMF0_XPEM"])

# 3. Download audio:
options = {
    "format": "bestaudio/audio",
}
dl = YoutubeDL(options)
dl.download(['https://www.youtube.com/watch?v=vtQk6EQnlQ4'])

# 4. Search and then download the first video:
options = {
    "default_search": "ytsearch",
    "max_download": 1,
}
dl = YoutubeDL(options)
dl.download(["IELTS speaking sample"])

# 5. Search and then download the first audio:
options = {
    "default_search": "ytsearch",
    "max_download": 1,
    "format": "bestaudio/audio",
}
dl = YoutubeDL(options)
dl.download(["Mikky Ekko - Time"])