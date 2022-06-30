<p align="center">
  <img width="460" height="300" src="https://i.ibb.co/ZYwfXVM/LMS-Notifier-Logo-Animasi-500-300-piksel-1.png">
</p>


Program Sederhana yang dibuat dengan Python3 dan Scraping ke web LMS ITTP untuk mendapatkan list tugas kemudian ditampilkan melalui Popup Notification. sebagai pengingat agar tidak lupa mengerjakan tugas kuliah



## Dibuat Dengan

 - [Python3](https://www.python.org/)
 - [Requests](https://pypi.org/project/requests/)
 - [BeautifulSoup](https://pypi.org/project/beautifulsoup4/)
 - [Win10Toast](https://pypi.org/project/win10toast/)
 - [InquirerPy](https://pypi.org/project/inquirerpy/)
 - [Configparser](https://docs.python.org/3/library/configparser.html)
 - [Schedule](https://pypi.org/project/schedule/)
 - [PyInstaller](https://pyinstaller.org/en/stable/)


## Fitur

| Fitur             |                                                                 |
| ----------------- | ------------------------------------------------------------------ |
| Pengaturan Waktu Notifikasi | ✅ |
| Pengaturan Akun disimpan di file config .ini | ✅ |
| Login Account Menggunakan Session Cookie | ✅ |
| Headless | ✅ |


## Penggunaan

Terdapat 2 cara penggunaan, bisa run dengan file main.py atau dengan membuka file yang telah dibuild menjadi 1 program Executable

```bash
  git clone https://github.com/sandrocods/lmsNotifier
  cd lmsNotifier
```
Install module requirements & Menjalankan main.py
```bash
  pip3 install -r requirements.txt
  python3 main.py
```

#### Atau dengan 

Menjalankan file .exe
```bash
  cd output
  .\lmsNotifier.exe
```

#### Konfigurasi awal
![App Screenshot](https://i.ibb.co/8BSBPRr/Screenshot-2.png)

| Parameter | Tipe     | Deskripsi                |
| :-------- | :------- | :------------------------- |
| `username` | `string` | **Required**. Username akun LMS kamu |
| `password` | `string` | **Required**. Password akun LMS kamu |
| `notification type` | `option` | **Required**. menit / jam |
| `notification delay` | `numeric` | **Required**. 1 / 60 / 120 |


## Screenshots



#### Notifikasi Autentikasi berhasil
![App Screenshot](https://i.ibb.co/bsJJYN2/Screenshot-3.png)


#### Notifikasi Autentikasi Gagal
![App Screenshot](https://i.ibb.co/nMbJyMP/Screenshot-6.png)

#### Notifikasi Informasi
![App Screenshot](https://i.ibb.co/dKBxyxJ/Screenshot-4.png)


#### Notifikasi tidak ada tugas
![App Screenshot](https://i.ibb.co/S6nLhkK/Screenshot-5.png)



## Support

Program ini bersifat open source jika ada error request issue saja untuk lebih lanjut bisa hubungi telegram saya 
https://t.me/Sandroputraaa

