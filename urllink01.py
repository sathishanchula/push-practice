import urllib.request

fhand = urllib.request.urlopen('urllink01http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())
