from collections import *
c = Counter()
string = 'ThiS is String with Upper and lower case Letters'
string = string.replace(' ','').lower()
x  = [*string]
c = Counter(x)
for k, v in sorted(c.items()):
    print(k,v)