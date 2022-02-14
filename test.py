import requests,pyfiglet,re,os,sys
from bs4 import BeautifulSoup as bs
from colorama import Fore, Back, Style
#############################################
os.system('cls' if os.name == 'nt' else 'clear')
os.system("color B")
ascii_banner = pyfiglet.figlet_format(" X Finder")
print(Fore.CYAN+ascii_banner)
#############################################
print(" \033[0;93m-------------------------------------------------------------------------------------------")
print("  Warning : Your Most Add http or https .. and add / in last link exmple https://example.com/ ")
print(" -------------------------------------------------------------------------------------------")
website = input("[+]"+Fore.CYAN+" Enter URL: "+Fore.YELLOW)
xtitle = input("[+]"+Fore.CYAN+" Enter Title Page 404: "+Fore.YELLOW)
endpoints = [endpoint.rstrip('\n') for endpoint in open('path.txt')]

for endpoint in endpoints:
        url = website+endpoint
        r = requests.get(url)
        soup = bs(r.content, 'lxml')
        gg = soup.select_one('title')
        if gg == None:
            continue
        else:
            gg = str(gg)
            ggggg = re.split('<title.*?>(.+?)</title>',gg)
            x = ggggg[-2]
            if x == xtitle:
                print(Fore.WHITE+"[+]"+Fore.RED+url)
            else:print(Fore.WHITE+"[+]"+Fore.GREEN+url)
