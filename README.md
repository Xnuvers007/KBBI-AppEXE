# KBBI-AppEXE

ini adalah KBBI (Kamus Besar Bahasa Indonesia)

klik sini jika kalian malas...!!!

  - [Masalah](https://github.com/Xnuvers007/KBBI-AppEXE/#masalah)
  - [gpedit.msc](https://github.com/Xnuvers007/KBBI-AppEXE/#gpeditmsc)
  - [Penggunaan Aplikasi](https://github.com/Xnuvers007/KBBI-AppEXE/#penggunaan-aplikasi)
  - [Windows, Linux, Termux dengan python](https://github.com/Xnuvers007/KBBI-AppEXE/#windows-linux-termux-python)
  - [Windows.exe](https://github.com/Xnuvers007/KBBI-AppEXE/#windows-exe)
  - [Linux.exe](https://github.com/Xnuvers007/KBBI-AppEXE/#linux-exe)
  - [Copyright](https://github.com/Xnuvers007/KBBI-AppEXE/#copyright)
  - [Tampilan](https://github.com/Xnuvers007/KBBI-AppEXE/#tampilan)

# Masalah

jika kalian mengalami masalah saat membuka Applikasi nya seperti ini :

![image](https://user-images.githubusercontent.com/62522733/172937163-084ede7d-85cc-4241-b8eb-8ab82a8af087.png)

kalian cukup :

  - Klik kanan pada programnya (exe)
  - kemudian pilih properties
  - cari menu Change settings for all users
  - ![image](https://user-images.githubusercontent.com/62522733/172937723-5f362bef-a817-4eb8-bea1-68a04fdf50f1.png)
  - centang pada bagian "Run This program as an administrator"
  - setelah itu apply, dan gunakan aplikasinya (exe)

Jika tidak bisa gunakan cara ke 2:

  - Pencet Windows + R
  - Ketik Regedit lalu enter
  - ![image](https://user-images.githubusercontent.com/62522733/172938466-81c1f69e-0577-465d-8cc9-496a32d1cd96.png)
  - lalu ke HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\
  - ![image](https://user-images.githubusercontent.com/62522733/172938846-cd78507b-dc02-431f-9c4f-844d33cdc070.png)
  - cari ValidateAdminCodeSignatures dan set data menjadi 0
  - ![image](https://user-images.githubusercontent.com/62522733/172939036-5f43e721-9c8a-41b9-ba8b-d2858fc6338c.png)
  - cari EnableUIADesktopToggle dan set data menjadi 0
  - ![image](https://user-images.githubusercontent.com/62522733/172939166-ba827056-9bc6-468e-a771-89a41eb5969f.png)
  - Tutup Registry editornya, dan restart komputer

Jika Tidak bisa, Gunakan cara ke 3

  - Pencet Windows + R
  - ketik gpedit.msc lalu enter
  - ![image](https://user-images.githubusercontent.com/62522733/172945904-981658a2-ba60-432f-b327-e6077497c05f.png)
  - lalu pergi ke arah Computer Configuration > Windows Settings > Security Settings > Local Policies > Security Options
  - ![image](https://user-images.githubusercontent.com/62522733/172945973-7ec07660-da09-4b86-b438-0d56ae2232b7.png)
  - Cari dan double click pada User Account Control: Only elevate executables that are signed and validated
  - ![image](https://user-images.githubusercontent.com/62522733/172946058-16802caf-cbde-4d78-993e-9c5cac3537eb.png)
  - lalu disabled
  - ![image](https://user-images.githubusercontent.com/62522733/172946081-5197b86a-cd6f-4c79-a4f9-fba5f806cceb.png)
  - lalu pada AllowUIAccess di disabled
  - ![image](https://user-images.githubusercontent.com/62522733/172946549-88979b24-0d3e-4bbc-a791-cfd82dfb5819.png)

# Gpedit.msc

Jika Kalian mengalami masalah pada gpedit.msc atau gpedit cannot found, silahkan ikutin cara ini:
  - silahkan download ini [di sini](https://github.com/Xnuvers007/KBBI-AppEXE/tree/master/gpedit%20if%20not%20found)
  - setelah itu run as administrator gpedit-enabler.bat atau jika tidak bisa, double click setup.exe
  - setelah itu pergi ke C:\Windows\SysWOW64
  - lalu copy/salin folder "GroupPolicy", "GroupPolicyUsers" dan gpedit.msc
  - setelah itu pencet windows + R dan ketik gpedit.msc
  - jika sudah berhasil dibuka saja , jika berhasil dibuka namun terdapat tulisan ***MMC cannot create a snap-in***
  - pergi ke  C:\Windows\Temp\gpedit\ pastikan folder tersebut ada
  - lalu copy x64.bat dan x86.bat [di sini](https://github.com/Xnuvers007/KBBI-AppEXE/tree/master/gpedit%20if%20not%20found) dan tempel ke C:\Windows\Temp\gpedit\ replace saja
  - jika sudah, klik kanan run as administrator dan jalankan sesuai operasi windows kamu, jika 32 bit maka pilih x86.bat, jika 64.bit maka pilih x64.bit
  - jika tidak mengetahui berapa bit, silahkan ketik windows + R ketik msinfo32 lalu cek pada bagian System Type
  - jika sudah dijalankan
  - setelah itu pergi ke C:\Windows\SysWOW64
  - lalu copy/salin folder "GroupPolicy", "GroupPolicyUsers" dan gpedit.msc
  - setelah itu pencet windows + R dan ketik gpedit.msc

# Penggunaan Aplikasi

# Windows, Linux, Termux (python)
jika punya python :
  1. download repo ini https://codeload.github.com/Xnuvers007/KBBI-AppEXE/zip/refs/heads/master
  2. cd KBBI-AppEXE
  3. python3 KBBI.py

# Windows (exe)
jika tak punya python (gunakan exe) :
  1. download repo ini https://codeload.github.com/Xnuvers007/KBBI-AppEXE/zip/refs/heads/master
  2. cd KBBI-AppEXE/Application
  3. double Click KBBI.exe

# Linux (exe)
jika menggunakan linux tanpa python (gunakan exe) :
  1. sudo su
  2. sudo apt-get install git
  3. git clone https://github.com/Xnuvers007/KBBI-AppEXE
  4. cd KBBI-AppExe/Application
  5. sudo dpkg --add-architecture i386
  6. sudo apt-get update
  7. sudo apt-get install wine
  8. sudo apt-get install wine32 win64 winbind winetricks
  9. wine --version
  10. wine KBBI.exe

# Tampilan

![image](https://user-images.githubusercontent.com/62522733/172957599-56878bdc-1359-4409-8405-c89bf7021217.png)

![image](https://user-images.githubusercontent.com/62522733/172957843-269d2816-6bd4-4a88-8045-8d84eb0796c8.png)

![image](https://user-images.githubusercontent.com/62522733/172957915-2ac9660c-6364-41f4-a9fc-2b72e7655146.png)

![image](https://user-images.githubusercontent.com/62522733/172957956-2e3a7e40-4e0f-4b60-837c-76bd04e29bbd.png)

# Copyright

Copyright (c) 2022 Xnuvers007 indradwi.25.
All Rights Reserved.

![image](https://user-images.githubusercontent.com/62522733/172956320-f2df83ea-3264-4e17-8d1f-95cc21eb0e8f.png)
