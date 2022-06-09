# KBBI-AppEXE
ini adalah KBBI (Kamus Besar Bahasa Indonesia)

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
  - 
