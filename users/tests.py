from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=9bZkp7q19f0')
video = yt.streams.first()
video.download('')
print(yt.title)