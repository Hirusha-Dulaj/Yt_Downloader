import youtube_dl

ydl_opts = {}

def dwl_vid():
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		ydl.download([zxt])

channel = 1
while (channel == int (1)):
	video_link = input("Youtube Video Link :  ")
	zxt = video_link.strip()

	dwl_vid()
	channel = int(input("Enter 1 if you want to download more videos \nEnter 0 if you are done : "))

