import urllib

__author__="Albert"
__date__ ="$Mar 12, 2012 4:38:05 PM$"

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
objects = []
data = []
clean = []
nothing = "12345"


#for i in range(403):
#    objects.append(urllib.urlopen(url+nothing))
#    data.append(objects[i].readline())
#    clean.append(data[i][-5:])
#    if clean[i][0]==' ':
#        nothing = clean[i][1:]
#    else:
#        nothing = clean[i]
returnstring = "and the next nothing is (\d+)"

while True:
    try:
        site = urllib.urlopen(url+nothing).read()
        nothing = re.search(returnstring, site).group(1)
    except:
        break
               
print clean
print nothing

    



