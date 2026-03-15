# Laporan Praktikum Jaringan Komputer (Week 2)
<br/>

## Nama : Yoga Perkasa Didik
## Nim  : 103072400106

## Mencakup cara
1. [Instalasi Python & Wireshark](#Instalasi)
2. [Testing wireshark](#Testing)
2. [Kesimpulan Praktikum](#Kesimpulan)

# Instalasi
## Python
>Instalasi python dapat dilakukan melalui website [python](https://www.python.org/downloads/)
![Download Python](/week2/img/PythonDownl.png)
Yang perlu dilakukan hanyalah
1. Download Python
2. Jalankan file exe
3. Cek versi python melalui command python --version di terminal dan where python untuk mengetahui dimana python di-instal.
![Cek Python](/week2/img/Pythoncmd.png)

## Wireshark
> Wireshark sendiri digunakan pada mapel jarkom untuk menganalisis, mengecek tipe protokol, dan melakukan troubleshoot melalui packet-packet jaringan yang muncul secara cepat pada software wireshark.
> Dapat di download di ![Wireshark](https://www.wireshark.org/download.html)
![Download Wireshark](/week2/img/WiresharkDownl.png)

# Testing 
> Pengetesan packet capture menggunakan wireshark
Tujuan dari praktikum ini adalah untuk mengetes apakah domain yang kita refresh dapat di tangkap oleh wireshark!. Pastikan untuk tidak menggunakan DNS seperti cloudflare karena terakhir kali dicoba di kelas, packet gagal tertangkap.

1. Jalankan Wireshark hingga muncul tampilan awal menyerupai dashboard
![Numero uno](/week2/img/Step1.png)
> Pilih opsi wifi dan ketuk 2 kali.
2. Di section ini, kita dapat melihat paket apa saja yang ditangkap oleh wireshark. Semua, mulai dari protokol jaringan, waktu, throughput, dan apapun yang berkaitan jaringan, cukup lengkap disini.
![Numero dua](/week2/img/Step2.png)
3. Pada modul, kita akan dibawa kesebuah link untuk melihat apakah request pada browser dapat ditangkap oleh wireshark (Matikan vpn atau dns agar masuk).
![Numero tiga](/week2/img/Step3.png)
> Jika tidak masuk, silahkan refresh web!.
![Numero empat](/week2/img/Step4.png)
> Ganti filter pada searchbar ke ** http ** agar kita dapat melihat request tersebut.


# Kesimpulan
Kesimpulan yang dapat saya telaah selama pembelajaran praktikum pekan dua adalah bagaimana kita bisa mengetahui jenis protokol
pada semua request yang terkirim di jaringan melalui satu software saja. Selain itu, saya juga dapat mempelajari bagaimana proses komunikasi data terjadi di jaringan, mulai dari pengiriman request oleh client hingga diterimanya response dari server.