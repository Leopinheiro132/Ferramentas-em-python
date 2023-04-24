# Imports
from googlesearch import search
from Modules.random import *
import time
import requests
import os

def checkvpn():
  c=os.system("ifconfig tun0")
  os.system("clear")
  if(c==0):
    banner()
    print("")
  else:
    banner()
    print("\033[1;31;40mSua VPN não existe ou não é boa para o uso.")
    print("")
  
def banner():
  os.system("clear")
  print('''\033[1;32;40m
   _____                  _                         
  / ____|                | |                        
 | |     __ _ _ __  _   _| |__   __ _ _ __ __ _     
 | |    / _` | '_ \| | | | '_ \ / _` | '__/ _` |    
 | |___| (_| | |_) | |_| | |_) | (_| | | | (_| |    
  \_____\__,_| .__/ \__, |_.__/ \__,_|_|  \__,_|    
             | |     __/ |                          
             |_|    |___/                           
            _____                                   
           / ____|                                  
          | (___   ___ __ _ _ __                    
           \___ \ / __/ _` | '_ \                   
           ____) | (_| (_| | | | |                  
          |_____/ \___\__,_|_| |_|                  
                                                    
                                                    ''')
  print("     \033[1;36;40m Developed by: \033[1;32;40m CapyHacker")
  print("           \033[1;36;40m Github: \033[1;32;40m www.github.com/EM ESPERA")

banner()
checkvpn()

headers={'User-Agent': random_agent()}
dork=str(input("\033[1;33;40mDigite a DORK: "))
num=int(input("\033[1;33;40mQuantos resultados voce quer procura?: "))
times=int(input("\033[1;33;40mDigite um tempo para espera: "))
op=str(input("\033[1;33;40mVoce quer salvar os sites vulneraveis em um arquivo?(Y,S/n,n) :"))

if(op=="Y" or op=="y" or op=="S" or op=="s"):
    name=str(input("\033[1;33;40mQual o nome do arquivo: "))
    print("\033[1;32;40mTodas as vunerabilidades salvas em: "+name)
    time.sleep(2)
    f=open(name,"a+")
i=1
banner()
checkvpn()
for url in search(dork,tld="com",num=num,stop=num,pause=2):
  if("php?" not in url):
    i=i+1
    continue   

  print("\033[1;37;40m"+str(i)+". \033[1;35;40mChecando a URL: ")
  print("\033[1;34;40m"+url)
  try:
    checkurl=url+"%27"
    proxy=randomProxy()
    print(f"usando essa proxy: {proxy}\n")
    r=requests.get(url,headers=headers, proxies={'http': proxy, 'https': proxy},timeout=times)
    s=requests.get(checkurl,headers=headers, proxies={'http': proxy, 'https': proxy},timeout=times)
    
    if((s.url != checkurl) or ("af.org.pk" in url)):
      print(f"\033[1;31;40m[Not Vul]--- {url}\n")
      i=i+1
      continue
    if(r.text==s.text):
      print(f"\033[1;31;40m[Not Vul]--- {url}\n")
    else:
      print(f"\033[1;32;40m[Vul]------- {url}\n")
    if(op=="Y" or op=="y"):
      f.write(url+"\n")   
  except:
    print("\033[1;31;40mEste site não pode ser acessado.")
    print("")
    i=i+1
try: 
  f.close()
  print("\033[1;32;40mUrl's salvas em: "+name)
except:
  pass

# End