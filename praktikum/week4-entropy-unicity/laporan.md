# Laporan Praktikum Kriptografi
Minggu ke-: 4
Topik: [Entropy Unicity]  
Nama: Ahmad Nur Kholis
NIM: 220202691
Kelas: 5 IKKA  

---

## 1. Tujuan
1. Menyelesaikan perhitungan sederhana terkait entropi kunci.
2. Menggunakan teorema Euler pada contoh perhitungan modular & invers.
3. Menghitung unicity distance untuk ciphertext tertentu.
4. Menganalisis kekuatan kunci berdasarkan entropi dan unicity distance.
5. Mengevaluasi potensi serangan brute force pada kriptosistem sederhana.


## 2. Dasar Teori
a. Entropy key
Jumlah ketidakpastian total dalam kunci.
Semakin besar ruang kunci → semakin besar entropinya.
b. Redudansi Pesan
Bahasa manusia tidak “random”.
Misal teks bahasa Inggris memiliki redundansi sekitar 50%.
Redundansi berarti sebagian ciphertext membawa informasi yang dapat diprediksi → dapat membantu penyerang.
c. Unicity Distance
Diperkenalkan oleh Shannon.
Dirumuskan sebagai:
    
    V = H(K)/R

Interpretasi:
Jumlah minimum ciphertext yang diperlukan agar kunci dapat ditentukan secara unik oleh penyerang.
d. Logika Intinya
- Jika ciphertext terlalu sedikit → banyak kemungkinan kunci yang menghasilkan plaintext “masuk akal”.
- Jika ciphertext melewati unicity distance → hanya satu kunci yang konsisten dengan statistik bahasa → kunci dapat ditemukan.

Nilai pentingnya
- Entropy unicity digunakan untuk:
- menilai kekuatan skema enkripsi,
- mengetahui kapan sistem rentan terhadap ciphertext-only attack,
- memahami batas keamanan fundamental menurut teori informasi.(a) Entropi Kunci (H(K))
- Jumlah ketidakpastian total dalam kunci.
- Semakin besar ruang kunci → semakin besar entropinya.

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

## 4. Langkah Percobaan
1. Perhitungan Entropi
Gunakan rumus:
[ H(K) = \log_2 |K| ]
dengan (|K|) adalah ukuran ruang kunci.
Contoh implementasi Python:
"import math

def entropy(keyspace_size):
    return math.log2(keyspace_size)

print("Entropy ruang kunci 26 =", entropy(26), "bit")
print("Entropy ruang kunci 2^128 =", entropy(2**128), "bit")
"
2. Menghitung Unicity Distance
Gunakan rumus:
[ U = \frac{H(K)}{R \cdot \log_2 |A|} ]
dengan:

(H(K)): entropi kunci,
(R): redundansi bahasa (misal bahasa Inggris (R \approx 0.75)),
(|A|): ukuran alfabet (26 untuk A–Z).
Contoh implementasi Python:
"def unicity_distance(HK, R=0.75, A=26):
    return HK / (R * math.log2(A))

HK = entropy(26)
print("Unicity Distance untuk Caesar Cipher =", unicity_distance(HK))"

3. Analisis Brute Force
Simulasikan waktu brute force dengan asumsi kecepatan komputer tertentu.

"def brute_force_time(keyspace_size, attempts_per_second=1e6):
    seconds = keyspace_size / attempts_per_second
    days = seconds / (3600*24)
    return days

print("Waktu brute force Caesar Cipher (26 kunci) =", brute_force_time(26), "hari")
print("Waktu brute force AES-128 =", brute_force_time(2**128), "hari") "
## 5. Source Code
import math

def entropy(keyspace_size):
    return math.log2(keyspace_size)

print("Entropy ruang kunci 26 =", entropy(26), "bit")
print("Entropy ruang kunci 2^128 =", entropy(2**128), "bit")
def unicity_distance(HK, R=0.75, A=26):
    return HK / (R * math.log2(A))

HK = entropy(26)
print("Unicity Distance untuk Caesar Cipher =", unicity_distance(HK))
def brute_force_time(keyspace_size, attempts_per_second=1e6):
    seconds = keyspace_size / attempts_per_second
    days = seconds / (3600*24)
    return days

print("Waktu brute force Caesar Cipher (26 kunci) =", brute_force_time(26), "hari")
print("Waktu brute force AES-128 =", brute_force_time(2**128), "hari")
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
1. Nilai entropi kunci menunjukkan seberapa besar ketidakpastian atau “kerandoman” kunci yang harus ditebak penyerang.
Semakin tinggi entropi → semakin sulit diprediksi → semakin besar jumlah kemungkinan yang harus dicoba penyerang.

2. Unicity distance adalah ukuran berapa banyak ciphertext yang cukup untuk mengeliminasi semua kemungkinan kunci kecuali satu.
Artinya:
Jika ciphertext yang terlihat < unicity distance → banyak kunci masih mungkin → keamanan tinggi.
Jika ciphertext > unicity distance → statistik pesan membantu penyerang menemukan kunci secara unik.

3. Brute force masih berbahaya karena:

    a. Kunci sering tidak random

        Manusia memilih password → entropi rendah → brute force efektif.

    b. Sistem autentikasi sering lemah

        Contoh:

        server tidak membatasi login attempts,

        hash password tidak dilindungi dengan salt,

        penggunaan algoritma hashing cepat (MD5, SHA1).

    c. Brute force tidak menyerang cipher modern

        Tetapi menyerang:

        implementasi yang salah,

        kunci yang pendek,

        perangkat yang bocor (side-channel),

        data yang di-leak di tempat lain.

    d. Kemajuan GPU/ASIC

        Hardware modern dapat mencoba miliaran kombinasi per detik.

        Kesimpulan: Brute force tetap ancaman bukan karena algoritmanya lemah, tetapi karena manusia dan implementasi sering tidak meningkatkan entropi kunci hingga setinggi yang diperlukan.

## 8. Kesimpulan
1. Caesar Cipher memiliki entropi rendah → mudah ditebak → unicity distance sangat kecil → brute force tidak relevan karena terlalu cepat.
Praktis: Tidak aman sama sekali.

2. AES-128 memiliki entropi sangat besar → unicity distance sangat besar → brute force tidak mungkin diselesaikan dalam skala kosmik.
Praktis: Sangat aman untuk penggunaan modern.

3. Secara teori informasi maupun komputasi, cipher klasik dan cipher modern berada di dua dunia yang sangat berbeda.

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

    week4-entropy-unicity )
```
