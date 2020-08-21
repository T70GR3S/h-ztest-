import requests
import re
import time
import random
from colorama import Fore,  Style 


def get(url):
    response = requests.get(url)
    expression = """<td height="20">([^<]+)</td>
<td>([^<]+)</td>"""

    if response.status_code == 200:
        a = re.findall(expression, response.text)
        return [__ for _ in a for __ in _]


print(Fore.CYAN+"-----Çıkmak İçin Q ye basınız----")
print(Style.RESET_ALL)
ilk_zaman = time.time()
while True:

    start = time.time()
    isimler = random.choice(get('https://huseyindemirtas.net/kullanici-adi-listesi-ad-soyad-listesi/'))
    print(Fore.RED+isimler)
    print(Style.RESET_ALL)

    user = input(Fore.LIGHTMAGENTA_EX+"Kelimeyi Gir: ")

    print(time.time() - start)
    if user == isimler:
        print("Doğru")
    elif user == "Q":
        break
    else:
        print('yanlış')

print("Çıkış Yapılıyor\nToplam Geçen Zaman =", time.time() - ilk_zaman)
