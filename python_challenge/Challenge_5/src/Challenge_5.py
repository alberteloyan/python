import urllib, pickle

url = "http://www.pythonchallenge.com/pc/def/banner.p"

object = urllib.urlopen(url)
data = pickle.load(object)

object.close()

for elt in data:
    print "".join([e[1]*e[0] for e in elt])

