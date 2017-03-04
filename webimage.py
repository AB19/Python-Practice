import urllib.request
import random

def DownloadWebImage (url):
    name = random.randrange(1,1000) # names of our downloads
    FullName = str (name) + ".jpeg" # names as stored in your file location
    urllib.request.urlretrieve (url, FullName)

DownloadWebImage ("https://thenewboston.com/images/video_categories/198.png")
    
