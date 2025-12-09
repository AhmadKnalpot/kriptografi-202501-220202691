# Laporan Praktikum Kriptografi
Minggu ke-: 9
Topik: [Digital Signature]  
Nama: Ahmad Nur Kholis
NIM: 220202691
Kelas: 5 IKKA   

## 1. Tujuan
1. Mengimplementasikan tanda tangan digital menggunakan algoritma RSA/DSA.
2. Memverifikasi keaslian tanda tangan digital.
3. Menjelaskan manfaat tanda tangan digital dalam otentikasi pesan dan integritas data.

## 2. Dasar Teori
Digital signature adalah mekanisme kriptografi yang digunakan untuk memastikan sebuah pesan benar-benar berasal dari pengirim yang sah (authenticity) dan tidak mengalami perubahan selama dikirim (integrity). Berbeda dari tanda tangan biasa, tanda tangan digital bekerja dengan prinsip kriptografi kunci publik, di mana pengirim menggunakan kunci privat untuk membuat tanda tangan, dan penerima memverifikasinya menggunakan kunci publik.

Prosesnya dimulai dengan melakukan hash terhadap pesan, lalu hasil hash tersebut dienkripsi menggunakan kunci privat pengirim sehingga menghasilkan signature. Ketika penerima menerima pesan, ia menghitung ulang hash pesan dan memverifikasi signature menggunakan kunci publik. Jika cocok, maka pesan dipastikan tidak dimodifikasi dan memang berasal dari pemilik kunci privat.

Fondasi keamanan digital signature bergantung pada sifat matematika yang sulit dipecahkan, seperti faktorisasi bilangan besar (RSA) atau elliptic curve discrete logarithm (ECDSA). Selain memastikan keaslian dan integritas, digital signature juga mendukung non-repudiation, yaitu pengirim tidak dapat menyangkal bahwa ia pernah menandatangani pesan tersebut.

## 3. Alat dan Bahan
- Python 3.11  
- Visual Studio Code
- Git dan akun GitHub  
- Library pycryptodome


## 4. Langkah Percobaan
1. Generate Key dan Buat Tanda Tangan
2. Verifikasi Tanda Tangan
3. Uji Modifikasi Pesan

## 5. Source Code
1. Generate Key dan Buat Tanda Tangan
    from Crypto.PublicKey import RSA
    from Crypto.Signature import pkcs1_15
    from Crypto.Hash import SHA256

    # Generate pasangan kunci RSA
    key = RSA.generate(2048)
    private_key = key
    public_key = key.publickey()

    # Pesan yang akan ditandatangani
    message = b"Hello, ini pesan penting."
    h = SHA256.new(message)

    # Buat tanda tangan dengan private key
    signature = pkcs1_15.new(private_key).sign(h)
    print("Signature:", signature.hex())

2. Verifikasi Tanda Tangan
    try:
        pkcs1_15.new(public_key).verify(h, signature)
        print("Verifikasi berhasil: tanda tangan valid.")
    except (ValueError, TypeError):
        print("Verifikasi gagal: tanda tangan tidak valid.")

3. Uji Modifikasi Pesan
    # Modifikasi pesan
    fake_message = b"Hello, ini pesan palsu."
    h_fake = SHA256.new(fake_message)

    try:
        pkcs1_15.new(public_key).verify(h_fake, signature)
        print("Verifikasi berhasil (seharusnya gagal).")
    except (ValueError, TypeError):
        print("Verifikasi gagal: tanda tangan tidak cocok dengan pesan.")
        
## 6. Hasil dan Pembahasan

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
