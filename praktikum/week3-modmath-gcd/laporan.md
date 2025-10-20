# Laporan Praktikum Kriptografi
Minggu ke-: 3 
Topik: Modular Math
Nama: Ahmad Nur Kholis
NIM: 220202691
Kelas: 5 IKKA  

---

## 1. Tujuan
Pada akhir sesi ini mahasiswa menghasilkan:

1. Perhitungan modular arithmetic & GCD menggunakan Python.
2. Identifikasi bilangan prima dan penerapan algoritma Euclidean.
3. Simulasi sederhana logaritma diskrit.
4. Commit kode perhitungan ke repositori dengan format week3-modmath-gcd.

## 2. Dasar Teori
Teori Modular Arithmetic dan GCD

Aritmetika modular merupakan cabang dari teori bilangan yang mempelajari operasi aritmetika dengan batasan tertentu yang disebut modulus. Dalam sistem ini, bilangan akan “berulang” setelah mencapai nilai modulus tersebut. 

Aritmetika modular memiliki beberapa sifat penting. Jika dua bilangan memenuhi kesetaraan modular, maka hasil penjumlahan, pengurangan, dan perkaliannya juga akan memenuhi kesetaraan modular dengan modulus yang sama. Selain itu, konsep invers modular juga penting, yaitu bilangan yang jika dikalikan dengan bilangan lain menghasilkan 1 dalam sistem modulus tertentu.

Sementara itu, GCD (Greatest Common Divisor) atau Faktor Persekutuan Terbesar (FPB) adalah bilangan bulat positif terbesar yang dapat membagi habis dua bilangan tanpa sisa. GCD dapat dihitung dengan berbagai cara, salah satunya menggunakan algoritma Euclid, yaitu metode pembagian berulang.

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan

1. Fungsi untuk menghitung operasi modular dasar.
2. Implementasikan fungsi GCD dengan algoritma Euclidean.
3. Tambahkan fungsi untuk mencari invers modular.
4. Simulasikan logaritma diskrit sederhana: mencari x sehingga a^x ≡ b (mod n).
---

## 5. Source Code
```python

def mod_add(a, b, n): return (a + b) % n
def mod_sub(a, b, n): return (a - b) % n
def mod_mul(a, b, n): return (a * b) % n
def mod_exp(base, exp, n): return pow(base, exp, n)



## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)


## 7. Jawaban Pertanyaan

    1. Peran Aritmetika Modular dalam Kriptografi Modern

    Aritmetika modular menjadi **dasar utama dalam kriptografi modern** karena digunakan untuk menjaga keamanan data melalui operasi bilangan besar yang sulit dibalik. Dalam sistem seperti **RSA**, **Diffie–Hellman**, dan **ElGamal**, semua perhitungan (seperti enkripsi dan dekripsi) dilakukan dengan operasi modular, misalnya ( c = m^e \mod n ).

    2. Pentingnya Invers Modular dalam Algoritma Kunci Publik (RSA)

    Invers modular digunakan untuk membalik proses enkripsi menjadi dekripsi.
    Dalam RSA, terdapat dua kunci:

    * Kunci publik: ((e, n))
    * Kunci privat: ((d, n))
    Tanpa invers modular ini, pesan yang terenkripsi tidak bisa dikembalikan ke bentuk aslinya.
    Invers modular adalah kunci agar enkripsi dan dekripsi bisa saling membatalkan dengan aman.

    3. Tantangan Utama dalam Menyelesaikan Logaritma Diskrit untuk Modulus Besar

    Masalah logaritma diskrit ( a^x = b (mod{n} )) **sangat sulit diselesaikan** jika modulus ( n ) besar. Tidak ada algoritma efisien untuk menemukan ( x ) dengan cepat ketika ( n ) memiliki ratusan atau ribuan bit.
    Karena tingkat kesulitannya yang tinggi, logaritma diskrit digunakan sebagai dasar keamanan pada sistem seperti Diffie–HellmanlGamal
    Tantangan utamanya adalah kompleksitas komputasi yang sangat besar, sehingga membuat sistem kriptografi menjadi aman.

## 8. Kesimpulan
    Program ini menunjukkan cara melakukan operasi aritmetika modular seperti tambah, kali, dan pangkat menggunakan Python. Fungsi gcd digunakan untuk mencari FPB, sedangkan modinv mencari invers modular. Ada juga discrete_log untuk mencari nilai eksponen pada persamaan modular. Secara umum, program ini membantu memahami penerapan dasar modular arithmetic dan GCD dalam pemrograman.    

## 9. Daftar Pustaka
1. Rosen, Kenneth H. (2012). Discrete Mathematics and Its Applications (7th ed.). McGraw-Hill.

2. Burton, David M. (2011). Elementary Number Theory (7th ed.). McGraw-Hill.

3. Stallings, William. (2017). Cryptography and Network Security: Principles and Practice (7th ed.). Pearson.

4. LeVeque, William J. (1990). Fundamentals of Number Theory. Dover Publications.

5. Weisstein, Eric W. (2023). “Modular Arithmetic” & “Greatest Common Divisor,” MathWorld – A Wolfram Web Resource. https://mathworld.wolfram.com


## 10. Commit Log

commit week3-modmath-gcd
Author: Ahmad Nur KHolis <email>
Date:   2025-10-20

    week3-modmath-gcd :  Modular Math & GCD 
```
