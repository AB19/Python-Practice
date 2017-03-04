import urllib.request
from urllib import request

InputUrl = input ("Enter the url of the csv file\n")


def DownloadCSV (InputUrl):
    response = request.urlopen (InputUrl)
    csv = response.read()
    csv_str = str (csv)
    print (csv_str)
    lines = csv_str.split ("\\n")
    print (lines)
    destination = r"C:\Users\AB\Desktop\YahooData.csv"
    fw = open (destination, 'w')
    for line in lines:
        fw.write (line + "\n")
    fw.close ()


DownloadCSV (InputUrl)
