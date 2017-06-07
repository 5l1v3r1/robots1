import sys

def spl(string, length):
  return ' '.join(string[i:i+length] for i in xrange(0,len(string),length))

def binS2int(string):
 # print string
  num=0
  count=1
  for i in range (0,8):
    num += int(string[i])*(128/count)
    count=count*2
  return num

fname="beepboop.txt"

f=open(fname)

lines=f.readlines()

f.close()

final=""
for line in lines:
  line=line.replace("beep",".")
  line=line.replace("boop","-") #this is backwards, but wanted to test
  #line=line.replace(" ","")
  line=line.replace("/","")
  line=line.replace("\n"," ")
  line=line.replace("\r"," ")
  #print line  
  final += line

print final
print "##########"

#next=spl(final,8)
#y=next.split(" ")
#for x in y:
#  a=binS2int(x)
#  print str(a)
#  print chr(a)
