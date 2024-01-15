from pytube import YouTube
from sys import argv
import time

# argv[1] = input("What is the link of the video?")
# yt = YouTube(argv[1])
# link = argv[1]

link = input("What is the link of the video? ")
yt = YouTube(link)

print("Title: ", yt.title)

print("View: ", yt.views)

yd = yt.streams.get_highest_resolution()
yd1 = str(yd)

print("\nStatistics: " + yd1 + "\n")

destination = input("Where do you want the file stored (Public Downloads)? ")
if destination == "":
	destination = '/Users/Public/Downloads'

yd.download(destination)

print("Your video is stored in the " + destination + " folder.\n")

time.sleep(5)
