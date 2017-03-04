import bs4 as bs
import urllib.request

SourceCode = urllib.request.urlopen ("https://www.facebook.com/abhilash.garimella.71").read()

#print (SourceCode)

MySoup = bs.BeautifulSoup (SourceCode, "lxml")

#print (MySoup)

#print (MySoup.title)
#print (MySoup.title.name) 
#print (MySoup.title.string) 

#print (MySoup.p)
#print (MySoup.p.name)
#print (MySoup.p.string) returns a para if it has no child tags
#print (MySoup.p.text) returns para with child tags as well

#print (MySoup.find_all ("title"))
#print (MySoup.find_all ("link"))
#print (MySoup.find_all ("img"))

#Combine find_all and para to print all the paras without tags

#for para in MySoup.find_all ("p"):
    #print (para.string)
    #print (para.text)

# get all the text from the page. not all websites use paragraph tags

#print (soup.get_text())

for url in MySoup.find_all ("a"):
    print (url.get("href"))


