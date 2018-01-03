import sys
import urllib
import requests
import inflect

L2I = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",range(26)))
I2L = dict(zip(range(26),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
num = ["ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE", "TEN"]
p=inflect.engine()

def shift(ciphertext,key):
  plaintext = ""
  for c in ciphertext.upper():
    if c.isalpha(): 
      plaintext += I2L[ (L2I[c] - key)%26 ]
    else: 
      plaintext += c
  return plaintext

def magic(string1):
  value1=0
  x=-1
  y=0
  if "PLUS" in cipher2:
    #print "[!] Addition found"
    x=string1.find("PLUS")
    y=4
    s=cutter(string1,x,y)
    #print s
    a=parseMe(s[0])
    b=parseMe(s[1])
    value1=a+b
  elif "TIMES" in cipher2:
    #print "[!] Multiplication found"
    x=string1.find("TIMES")
    y=5
    s=cutter(string1,x,y)
    #print s
    a=parseMe(s[0])
    b=parseMe(s[1])
    value1=a*b
  elif "DIVIDE" in cipher2:
    #print "[!] Division found"
    x=string1.find("DIVIDE")
    y=6
    s=cutter(string1,x,y)
    #print s
    a=parseMe(s[0])
    b=parseMe(s[1])
    value1=a/b
  elif "MINUS" in cipher2:
    #print "[!] Subtraction found"
    x=string1.find("MINUS")
    y=5
    s=cutter(string1,x,y)
    #print s
    a=parseMe(s[0])
    b=parseMe(s[1])
    value1=a-b
  return value1
  #return s

def cutter(string,start,length):
  string1=string[:start]
  string2=string[(start+length):]
  final = [ string1 , string2 ]
  return final

def parseMe(input):
  for i in num:
    if i == input:
      return num.index(i)

url="http://haai.hackeducate.com/neuralnet.php"
session = requests.Session()
params= {"command":"authenticate"}
data= urllib.urlencode(params)
headers = {'Content-Type':'application/x-www-form-urlencoded'}
cookie= {'auth' :'MTo6QGJhc2g9VzM0R1MySTBZTEdBIQ%3D%3D'}

mkey, eauth = False, False

for i in xrange(1024):
  r = session.post(url,cookies=cookie,data=data,headers=headers)
  content = r.text
  if mkey and eauth:
    data={u'command':'destroy voxnihili'}
    break
  
  if "KEY" in content:
    print content[:content.find("Requested")]
    if "MASTERKEY" in content:
      mkey = True
    if "ENDAUTH" in content:
      eauth=True
  elif i < 10:
    #print "\n\n#####"+content+"\n"
    c3 = content.split(']')
    chall=c3[0].split('/')[1]
    key=c3[1].split(':')[1]
    cipher=c3[2].split(':')[1]

    cipher2 = shift(cipher,int(key))
    #print "[!] Decoded text: " + cipher2
    cipher3=magic(cipher2)
    #print "[!] Calculated response: "+str(cipher3)

    cipher4=p.number_to_words(cipher3)
    key2= 26-int(key)
    cipher4=shift(cipher4,int(key2))
    #print "[!] Sending ciphered text of: "+cipher4
    params= {"command":str(cipher4.upper())}
    data= urllib.urlencode(params)
  else:
    #print content
    data= {u'command':'status 4,294,967,295'}

r = session.post(url,cookies=cookie,data=data,headers=headers)
content = r.text
print "\n[!] Win???\n\n "+ content