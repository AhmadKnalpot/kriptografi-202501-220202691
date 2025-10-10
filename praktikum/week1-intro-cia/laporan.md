# Laporan Praktikum Kriptografi
Minggu ke-: 1
Topik: [Praktikum Kriptografi]  
Nama: [Ahmad Nur Kholis]  
NIM: [220202691]  
Kelas: [5 IKKA]  

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:

1. Menjelaskan sejarah dan evolusi kriptografi dari masa klasik hingga modern.
2. Menyebutkan prinsip Confidentiality, Integrity, Availability (CIA) dengan benar.
3. Menyimpulkan peran kriptografi dalam sistem keamanan informasi modern.
4. Menyiapkan repositori GitHub sebagai media kerja praktikum.

## 2. Dasar Teori
a. Cipher klasik adalah metode penyandian pesan yang digunakan sebelum munculnya teknologi komputer modern. Prinsipnya yaitu mengubah huruf-huruf dalam teks asli (plaintext) menjadi huruf lain (ciphertext) menggunakan pola tertentu agar pesan sulit dipahami oleh pihak lain. Contoh cipher klasik yang terkenal adalah Caesar Cipher yang menggeser huruf beberapa langkah, dan Vigenère Cipher yang menggunakan kunci kata untuk menentukan pergeseran. Meskipun sederhana, metode ini menjadi dasar perkembangan kriptografi selanjutnya.

b. Konsep modular aritmetika merupakan perhitungan dengan hasil yang dibatasi oleh suatu bilangan tertentu yang disebut modulus. Misalnya, 
10mod3=1, karena sisa hasil bagi 10 dibagi 3 adalah 1. Dalam kriptografi, konsep ini digunakan untuk menjaga agar hasil pergeseran huruf tetap berada dalam alfabet. Modular aritmetika juga menjadi dasar bagi berbagai algoritma kriptografi modern seperti RSA dan Diffie-Hellman.

c. Hubungan antara cipher klasik dan modular aritmetika dapat dilihat dari cara enkripsinya. Misalnya   pada Caesar Cipher digunakan rumus 
                        𝐶=(𝑃+𝑘)mod26C=(P+k)mod26
 di mana P adalah huruf asli, k jumlah pergeseran, dan C huruf hasil enkripsi. Dengan sistem ini, jika pergeseran melebihi jumlah huruf alfabet, hasilnya akan kembali ke awal secara otomatis. Jadi, modular aritmetika berperan penting dalam menjaga agar proses enkripsi dan dekripsi berjalan dengan benar.
 
## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file `caesar_cipher.py` di folder `praktikum/week2-cryptosystem/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python caesar_cipher.py`.)

---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
# contoh potongan kode
def encrypt(text, key):
    return ...
```
)

---

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

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: …  
- Pertanyaan 2: …  
)
---

## 8. Kesimpulan
(Tuliskan kesimpulan singkat (2–3 kalimat) berdasarkan percobaan.  )

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit abc12345
Author: Nama Mahasiswa <email>
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
