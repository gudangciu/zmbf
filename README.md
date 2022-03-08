#### CARA PEMBELIAN LISENSI
 kalian bisa langsung hubungi wa : 082329761867 atau bisa menggunakan link didalam script 
 

#### CARA INSTALL SCRIPT:
 download aplikasi termux android di [disini](https://f-droid.org/repo/com.termux_118.apk)
 lalu buka aplikasinya ketikan perintah dibawah ini.
 ```
 $ pkg update && pkg upgrade
 $ pkg install python git
 $ python -m pip install -r requirements.txt
 $ rm -rf zmbf
 $ git clone https://github.com/Fall-Xavier/zmbf
 $ cd zmbf
 $ cythonize -i zmbf.c
 $ python run.py
 ```
#### CARA MENJALANKAN SCRIPT:
 karna sudah pernah menginstall script jadi kita tinggal ketikkan ini untuk menjalankannya
 ```
  $ cd zmbf
  $ python run.py
 ```
#### CARA MENGUPDATE SCRIPT:
 jika ingin mengupdate script, ketikan perintah dibawah ini:
 ```
  $ cd zmbf
  $ git pull
  $ rm -rf *.so
  $ cythonize -i zmbf.c
  $ python run.py
 ```

