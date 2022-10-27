import requests,os,bs4
from pathlib import Path

r=requests.request("POST",'https://sms.sellaite.com/index_smssend.php')

if r.status_code !=200:
    print("network Error")
    exit()
e=int(input("country code-:"))
if len(str(e))>=4:
    print("country code only")
num=int(input("enter number:"))
msg=input("enter message or text file path -:")
if msg=='' or msg.isspace()==True:
    exit()
path = Path(msg)

way=path.is_file()

if way==True:


    ok=open(msg,'r')
    ok=ok.read()
    message=ok
  
    
else:
    message=msg

os.system('bash tempmail.sh -g > file.txt')
kk=open('file.txt','r')

k=kk.read().strip()
headers={"User-Agent ":"Mozilla/5.0 (X11; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0","Accept-Language":" en,hi;q=0.5","Accept-Encoding":" gzip, deflate","Referer":"https://sms.sellaite.com/index_smssend.php",'Content-type': 'application/x-www-form-urlencoded',"Origin":" https://sms.sellaite.com","Sec-Fetch-Dest": "document","Sec-Fetch-Site":" same-origin","Sec-Fetch-Mode":" navigate"}
print(k)
head={"User-Agent ":"Mozilla/5.0 (X11; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0"}
#form_email=pirofoc370%40abudat.com&form_countrycodenumber=91&form_ccode=91&form_phonenumber=7742114180&form_message=n&element_6_1=1&submitID=1&submitInfo=
h={"User-Agent ":"Mozilla/5.0 (X11; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0"}
sellaite=requests.request("POST",'https://sms.sellaite.com/index_smssend.php',data={"form_email":k,"form_countrycodenumber":e,"form_ccode":e,"form_phonenumber":num,"form_message":message,"element_6_1":1,"submitID":1,"submitInfo":' '}) 

# print(sellaite.content)
## trans id  trans num find
s=bs4.BeautifulSoup(sellaite.content,'html.parser')
try:
    ki=str(s.find_all(id='trans_id')).split('value="')[1].rstrip('"/>]')
    kkk=str(s.find_all(id='trans_num')).split('value="')[1].rstrip('"/>]')
    
    print(ki,'\n',kkk)

    tid=ki.strip()
    tn=kkk.strip()
except:
    print("error occured\n try again")
    exit()

#os.system("bash tempmail.sh -l| tail -n 1 > otp.txt")

#s.system("awk -F 'CODE: ' '{print  $2}' otp.txt > verify.txt")



def func():
    os.system("bash tempmail.sh -l| tail -n 1 > otp.txt")

    os.system("awk -F 'CODE: ' '{print  $2}' otp.txt > verify.txt")

    global otp
    o=open('verify.txt','r')
    otp=o.read().strip(r' \n ')
    return otp
import time
time.sleep(2)
func()
while str(otp)=='' or str(otp).isspace()==True:
    func()
otp=int(otp)
cook=sellaite.cookies.get_dict()
sellaite=requests.request("POST","https://sms.sellaite.com/index_smssend.php",cookies=cook,data={"form_code":otp,"trans_num":tn,"trans_id":tid,"uk":' '})
if sellaite.status_code==200:
    print("successful")
