import urllib.request
u = 'http://www.amazon.com/s/ref=nb_sb_noss?field-keywords=raspberry+pi'
f = urllib.request.urlopen(u)
contents = f.read()
print(contents)
f.close()
