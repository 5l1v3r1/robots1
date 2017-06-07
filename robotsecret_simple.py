#!/usr/bin/env python

import urllib
import urllib2

url="http://robots.hackeducate.com/robotssecretserver.php"
headers ={'Cookie':'auth=d296d449db7f938|1486564134|0110001101101101001110010110100101100010001100110101001001111010|cm9ib3RzMQ=='}

req = urllib2.Request(url,"",headers)

response=urllib2.urlopen(req)
content =response.read()

print content

c1=content.split(":")
c2=c1[1].split("+")
z=0
for x in c2:
  if "\r" in x:
    x=x.split("\r")[0]
  y=int(x)
  z+=y

zz=str(z)
print "Answer: "+zz

url="http://robots.hackeducate.com/door.php?answer="+zz
req = urllib2.Request(url,"",headers)

response=urllib2.urlopen(req)
content =response.read()

print content
