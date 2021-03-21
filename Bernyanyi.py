#!/bin/python

import os,sys,time

def bersih():
    os.system("clear")

def menu():
    bersih()
    print "+----------------------------------------------+"
    print "Author : Wafa"
    print "Youtube : Nanti Gw Buat :v"
    print "Github : Akun Github Gw Ilang :v"
    print "+----------------------------------------------+"
    print " [1] Install Nmap (No Root)"
    print " [2] Install Metasploit (No Root)"
    print " [3] Install Hack Wifi (Root)"
    print " [0] Keluar/Exit"
    pil = raw_input("Pilih Sesuai Nomor -> ")
    if pil =="1":
	os.system("pkg install unstable-repo")
	os.system("pkg install nmap")
	os.system("python2 Bernyanyi.py")
    elif pil =="2":
	os.system("pkg update && pkg upgrade")
	os.system("pkg install python -y")
	os.system("pkg install git -y")
	os.system("gem install lolcat")
	os.system("git clone https://github.com/noob-hackers/m-wiz")
	os.system("cd m-wiz")
	os.system("ls")
	os.system("bash m-wiz.sh")
	os.system("cd")
	os.system("msfconsole")
	os.system("python2 Bernyanyi.py")
    elif pil =="3":
	os.system("apt update")
	os.system("apt upgrade")
	os.system("apt install wget")
	os.system("apt install proot")
	os.system("pkg install curl")
	os.system("pkg install clang")
	os.system("pkg install tsudo")
	os.system("pkg install tsu")
	os.system("git clone https://github.com/kumpulanremaja/wifi")
	os.system("cd wifi")
	os.system("chmod +x wifi.sh")
	os.system("sh wifi.sh")
	os.system("python2 Bernyanyi.py")
    elif pil =="0":
        sys.exit()




menu()
