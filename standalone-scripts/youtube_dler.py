import pytube

video_url = input("Write your video url:")
yt = pytube.YouTube(video_url)

stream = yt.streams.get_highest_resolution()
print("Video is being downloaded!")
stream.download()