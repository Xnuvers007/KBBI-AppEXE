#/usr/bin/python3
#!/usr/bin/python3
#!/usr/bin/env python3
# Path: KBBI.py

# Created By Xnuvers007 (Indonesian , instagram : indradwi.25)

import time, os, sys, threading, itertools
from sys import platform

sys.setrecursionlimit(5000)
sys.getrecursionlimit()

Cyan='\033[0;36m'
reset='\033[0m'

os.system("clear||cls")

done = False

#print("please wait, sedang mengecek versi python")
def animate():
    print(Cyan + " ")
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rMohon Menunggu, Sedang mengecek versi Python ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
        if not sys.version_info.major==3 and sys.version_info.minor >= 6:
            print("Harap gunakan python versi 3.6 keatas")
            os.system("xdg-open https://python.org/download")
            sys.exit(1)
        sys.stdout.write('\rSelesai, Silahkan Pilih Menu')
    os.system("clear||cls")
    print(reset + " ")

t=threading.Thread(target=animate)
t.start()
time.sleep(5)
done = True

try:
    # Import random module for scrapping website
    import requests
    from requests.models import HTTPError
    # Import BeautifulSoup module for parsing HTML
    from bs4 import BeautifulSoup
except ModuleNotFoundError:
    if platform=="linux" or platform=="linux2":
        os.system("pip3 install requests")
        os.system("pip3 install beaufitulsoup4")
    elif platform=="win32":
        os.system("pip install requests")
        os.system("pip install beautifulsoup4")
    else:
        print("Cannot detect this device")
        os.system("exit")

usercontrol = os.getlogin()

__author__="Xnuvers007"
__copyright__="Copyright (c) 2022 Xnuvers007"
__license__="MIT"
__version__="1.1"

localtime = time.asctime(time.localtime(time.time()))

try:
    file = open("./Kbbi.txt", "a")
except FileExistsError:
    pass

def menu():
    print("============================================")
    print("Welcome to the Kamus Besar Bahasa Indonesia".upper())
    print("Selamat datang {}".format(usercontrol))
    print("Dicari Sejak : ", localtime)
    print("Created by Xnuvers007\n instagram: @indradwi.25")
    print("============================================")
    print("| 1. mencari Kata (misal: cabai, ambyar, dll.")
    print("| 2. Mencari kata yang benar (misal: cabai-atau-cabe, hancur atau ancur")
    print("============================================\n")
    print(" [+] === CTRL + C to Exit === [+] ")
    global pilih

def pilihan():
    try:
        pilih = int(input("Masukkan pilihan anda: "))
    except ValueError:
        print("Pilihan tidak ada")
        for i in range(1,4):
            i += 0
            print(i)
        menu()
    except (KeyboardInterrupt,UnboundLocalError):
        for i in range(1,4):
            i += 0
            print(i)
        os.system("exit")
    
    if pilih == 1:
        os.system("clear||cls")
        print("mencari Kata (misal: cabai, ambyar, dll.")
        print("============================================", file=file)
        print("Welcome to the Kamus Besar Bahasa Indonesia".upper(), file=file)
        print("Dicari Sejak : ", localtime, file=file)
        print("Created by Xnuvers007\nInstagram: @indradwi.25", file=file)
        print("============================================",file=file)
        try:
            kata = str(input("Masukkan kata yang ingin dicari: "))
        except ValueError:
            print("Kata tidak boleh kosong")
            for i in range(1,4):
                i += 0
                time.sleep(1)
                print(i)
            menu()
        except KeyboardInterrupt:
            for i in range(1,4):
                i += 0
                time.sleep(1)
                print(i)
            os.system("exit")
        url = "https://kbbi.web.id/"+kata
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63'}
        try:
            response = requests.get(url,headers=headers)
            soup = BeautifulSoup(response.text, "html.parser")
        except (ConnectionError,Exception, "HTTPError||TabError"):
            print("Nyalakan Internet terlebih dahulu")
            try:
                input("tekan enter jika sudah dinyalakan")
            except KeyboardInterrupt:
                for i in range(1,4):
                    i += 0
                    time.sleep(1)
                    print(i)
                os.system(exit)

            for i in range(1,4):
                i += 0
                print(i)
            os.system("exit")

        print("\n")
        print("============================================")
        print("Hasil pencarian kata: {kata}".format(kata=kata))
        print("Hasil pencarian kata: {kata}".format(kata=kata),file=file)
        print("============================================")
        try:
            print("Kata Dasar = ",soup.find("div", {'id': "w1"}).text)
            print("Kata Dasar = ",soup.find("div", {'id': "w1"}).text, file=file)
        except UnboundLocalError:
            os.system("exit")
        print("\n")
        # for kata in "div", {'id': "d1"},soup.find.text:
        try:
            ab = soup.find("div", {'id': "d1"}).text
            print(ab)
            print(ab, file=file)
        except UnboundLocalError:
            os.system("exit")
        try:
            ulang = str(input("Apakah anda ingin mengulang lagi ? [Y/n] : "))
        except (KeyboardInterrupt,Exception):
            for i in range(1,4):
                i += 0
                print(i)
            os.system("exit")
        if (ulang=='y' or ulang=='Y'):
            menu()
            pilihan()
        elif (ulang=='n' or ulang=='N'):
            keluar()
        else:
            keluar()

    elif pilih == 2:
        print("============================================", file=file)
        print("Welcome to the Kamus Besar Bahasa Indonesia".upper(), file=file)
        print("Dicari Sejak : ", localtime, file=file)
        print("Created by Xnuvers007\nInstagram: @indradwi.25", file=file)
        print("============================================",file=file)
        os.system("clear||cls")
        try:
            print("Masukan kata pertama dan kata kedua Contoh :")
            print("cabai-atau-cabe, hancur-atau-ancur")
            print("Tapi tidak menggunakan '-atau-' kalian hanya menginputkan 2 kata\n")
            kata = str(input("Masukkan kata yang ingin dicari 1 : "))
            kata1 = str(input("Masukkan kata yang ingin dicari 2 : "))
            kata2 = kata,"-atau-",kata1
            kt = str(kata2)
        except ValueError:
            print("Kata tidak boleh kosong")
            for i in range(1,4):
                i += 0
                time.sleep(1)
                print(i)
            menu()
        except KeyboardInterrupt:
            for i in range(1,4):
                i += 0
                time.sleep(1)
                print(i)
            os.system("exit")

        url = "https://kbbi.web.id/"+kt
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63'}
        try:
            response = requests.get(url,headers=headers)
            soup = BeautifulSoup(response.text, "html.parser")
        except (ConnectionError,Exception, "HTTPError||TabError"):
            print("Nyalakan Internet terlebih dahulu")
            input("tekan enter jika sudah dinyalakan")
            for i in range(1,4):
                i += 0
                print(i)
            os.system("exit")

        print("\n")
        print("============================================")
        print("Hasil pencarian kata: {kata} atau {kata1}".format(kata=kata, kata1=kata1))
        print("Hasil pencarian kata: {kata} atau {kata1}".format(kata=kata, kata1=kata1),file=file)
        print("============================================")

        try:
            data1 = soup.find('ul') # Find the first <ul> tag in the page
            for li in data1.find_all("li"):
                # a = li, end=", "
                print("Kata Dasar : ", li.text, end="\n", file=file)
                print("Kata Dasar : ", li.text, end="\n")
        except UnboundLocalError:
            os.system("exit")
        print("\n")
        try:
            print(soup.find("div", {'id': "d1"}).text, file=file)
            print(soup.find("div", {'id': "d1"}).text)
        except UnboundLocalError:
            os.system("exit")
        print("\n")
        try:
            ulang = str(input("Apakah anda ingin mengulang lagi ? [Y/n] : "))
        except ValueError:
            for i in range(1,4):
                i += 0
                time.sleep(1)
                print(i)
            menu()
        except KeyboardInterrupt:
            for i in range(1,4):
                i += 0
                time.sleep(1)
                print(i)
            os.system("exit")

        if (ulang=='y' or ulang=='Y'):
            menu()
            pilihan()
        elif (ulang=='n' or ulang=='N'):
            keluar()
        else:
            keluar()
    else:
        print("Pilihan tidak ada")
        keluar()

def keluar():
    print("Akan Keluar dalam 3 detik")
    for keluar in range (1,4):
        keluar += 0
        print(keluar)
    os.system("exit")

menu()
pilihan()
file.close()
