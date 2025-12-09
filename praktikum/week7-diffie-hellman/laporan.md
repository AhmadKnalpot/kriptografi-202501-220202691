# Laporan Praktikum Kriptografi
Minggu ke-: 7
Topik: [Diffie Hellman]  
Nama: Ahmad Nur Kholis
NIM: 220202691
Kelas: 5 IKKA    

---

## 1. Tujuan
1. Melakukan simulasi protokol Diffie-Hellman untuk pertukaran kunci publik.
2. Menjelaskan mekanisme pertukaran kunci rahasia menggunakan bilangan prima dan logaritma diskrit.
3. Menganalisis potensi serangan pada protokol Diffie-Hellman (termasuk serangan Man-in-the-Middle / MITM).

## 2. Dasar Teori
Diffie–Hellman adalah protokol pertukaran kunci yang memungkinkan dua pihak menghasilkan kunci bersama tanpa saling mengirimkan kunci rahasia secara langsung. Keamanannya bertumpu pada Discrete Logarithm Problem (DLP), yaitu sulitnya menghitung eksponen dari hasil perpangkatan dalam grup modular besar.

Protokol ini bekerja dengan memilih bilangan publik g dan p, lalu masing-masing pihak memilih nilai rahasia pribadi untuk dihitung sebagai nilai publik yang dibagikan. Meskipun nilai publik ini diketahui semua orang, menemukan nilai rahasia dari eksponen tersebut dianggap tidak praktis secara komputasi.

Kedua pihak kemudian menggabungkan nilai publik lawan dengan rahasia pribadi masing-masing, yang secara matematis menghasilkan kunci bersama yang identik. Dengan cara ini, Diffie–Hellman menyediakan fondasi bagi mekanisme enkripsi aman modern tanpa harus bertukar kunci secara fisik.

## 3. Alat dan Bahan
(- Python 3.11  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
1. Simulasi Diffie-Hellman
2. Analisis Serangan MITM (Man-in-the-Middle)

## 5. Source Code
    import random

    # parameter umum (disepakati publik)
    p = 23  # bilangan prima
    g = 5   # generator

    # private key masing-masing pihak
    a = random.randint(1, p-1)  # secret Alice
    b = random.randint(1, p-1)  # secret Bob

    # public key
    A = pow(g, a, p)
    B = pow(g, b, p)

    # exchange public key
    shared_secret_A = pow(B, a, p)
    shared_secret_B = pow(A, b, p)

    print("Kunci bersama Alice :", shared_secret_A)
    print("Kunci bersama Bob   :", shared_secret_B)

## 6. Hasil dan Pembahasan
Berikut hasil simulasi serangan di mana Eve mencegat dan mengganti public key:

Public key asli:
Alice (A) = 8
Bob (B) = 19
Public key palsu dari Eve:
Eve (E) = 17
Kunci yang dihitung Alice: 12
Kunci yang dihitung Bob: 15
Kunci yang diketahui Eve:
Dengan Alice → 12
Dengan Bob → 15

Hasilnya :
Alice dan Bob memiliki kunci berbeda, dan Eve mengetahui keduanya, sehingga komunikasi mereka dapat disadap.

## 7. Jawaban Pertanyaan
1. Karena nilai publik yang ditukar (misalnya g^a mod p dan g^b mod p)
tidak memungkinkan pihak luar menghitung nilai rahasia a dan b. Masalah matematis yang mendasari—Discrete Logarithm Problem—sangat sulit dipecahkan secara komputasi. Hanya kedua pihak yang mengetahui eksponen rahasia sehingga mereka dapat membentuk kunci bersama tanpa pernah mengirimkan kunci itu sendiri.
2. elemahan utamanya adalah tidak ada autentikasi. Siapa pun dapat menyamar sebagai pihak lain dan mengganti public key dalam proses pertukaran. Akibatnya, protokol DH murni rentan terhadap Man-in-the-Middle (MITM) meskipun perhitungan matematisnya aman.
3. Dengan menambahkan autentikasi ke proses pertukaran kunci. Ini dapat dilakukan menggunakan:
    - Tanda tangan digital (RSA, ECDSA) untuk membuktikan identitas pihak yang mengirim public key.
    - Sertifikat digital (PKI/SSL) seperti pada HTTPS.
    - HMAC + pre-shared key pada sistem tertutup.
    - Protokol modern seperti Authenticated Diffie–Hellman (ADH), ECDHE + TLS, atau Signal X3DH.

## 8. Kesimpulan
Diffie–Hellman memungkinkan dua pihak membuat kunci rahasia bersama tanpa pernah mengirimkan kunci tersebut secara langsung. Keamanannya bertumpu pada sulitnya memecahkan Discrete Logarithm Problem, sehingga nilai publik tidak cukup untuk menebak nilai rahasia. Dengan mekanisme ini, kedua pihak dapat membangun saluran aman meskipun berkomunikasi lewat jaringan yang tidak terpercaya.

## 9. Daftar Pustaka
- Stallings, W. *Cryptography and Network Security*.  

## 10. Commit Log

week7-diffie-hellman