import urllib.request
from urllib.request import urlopen
import os
import time
import sys
import pyfiglet
from colorama import Fore, Back, Style
#############################################
os.system('cls' if os.name == 'nt' else 'clear')
os.system("color B")
ascii_banner = pyfiglet.figlet_format(" X Finder")
print(ascii_banner)
#############################################
def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
time.sleep(0.5)
################### Menu ####################
def menu():
    print(" \033[1;33m[1] \033[1;96mFind Admin Panel ")
    print(" \033[1;33m[2] \033[1;96mFind Shell ")
    print(" \033[1;33m[99] \033[1;96mExit")
#############################################
def option1():
	print(" \033[0;93m-------------------------------------------------------------------------------------------")
	print("  Warning : Your Most Add http or https .. and add / in last link exmple https://example.com/ ")
	print(" -------------------------------------------------------------------------------------------")

	url = input('\033[1;96m'" Enter Website =====> "'\033[1;92m')
	print ("\033[1;96m")

	passee = str(urlopen("https://raw.githubusercontent.com/0xred/shellname/main/adminpanel.txt").read(), 'utf-8')
	for i in passee.split('\n'):
		curll = url+i
		try :
			openurl = urllib.request.urlopen(curll)
			print("\033[1;92m   Found   \033[1;96m<====> \033[1;92m"+curll,'\033[1;96m')
		except urllib.error.URLError as msg :
				print ("\033[1;91m Not Found \033[1;96m<====> \033[1;91m"+curll,'\033[1;96m')
################ function 2 #################
def option2():
	print(" \033[0;93m-------------------------------------------------------------------------------------------")
	print("  Warning : Your Most Add http or https .. and add / in last link exmple https://example.com/ ")
	print(" -------------------------------------------------------------------------------------------")
	url = input('\033[1;96m'" Enter Website =====> "'\033[1;92m')

	print ("\033[1;96m")
	passe = str(urlopen("https://raw.githubusercontent.com/0xred/shellname/main/shell.txt").read(), 'utf-8')
	for ss in passe.split('\n'):
		curl = url+ss
		try :
			openurl = urllib.request.urlopen(curl)
			print("\033[1;92m   Found   \033[1;96m<====> \033[1;92m"+curl,'\033[1;96m')
		except urllib.error.URLError as msg :
				print ("\033[1;91m Not Found \033[1;96m<====> \033[1;91m"+curl,'\033[1;96m')
################### Menu ####################
menu()
option = int(input(" \033[1;33mEnter Your Option: "))

while option != 99:
    if option == 1:
        option1()
    elif option == 2:
        option2()
    else:
        print(" Invalid option.")

    print()
    menu()
    option = int(input(" \033[1;33mEnter Your Option: "))

print(" \033[1;33m See You Late .... ") 
