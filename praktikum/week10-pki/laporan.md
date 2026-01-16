# Laporan Praktikum Kriptografi
Minggu ke-: 10
Topik: [Public Key Infrastrucuture]  
Nama: Ahmad Nur Kholis
NIM: 220202691
Kelas: 5 IKKA    

---

## 1. Tujuan
    1. Membuat sertifikat digital sederhana.
    2. Menjelaskan peran Certificate Authority (CA) dalam sistem PKI.
    3. Mengevaluasi fungsi PKI dalam komunikasi aman (contoh: HTTPS, TLS).

## 2. Dasar Teori
    Public Key Infrastructure (PKI) merupakan suatu kerangka kerja keamanan yang digunakan untuk menjamin kerahasiaan, keaslian, integritas, dan keabsahan komunikasi data dalam jaringan terbuka. PKI memanfaatkan kriptografi kunci publik dengan pasangan kunci publik dan kunci privat, di mana kunci publik digunakan untuk enkripsi atau verifikasi tanda tangan digital, sedangkan kunci privat digunakan untuk dekripsi atau pembuatan tanda tangan digital. Dengan mekanisme ini, PKI mampu mengatasi permasalahan kepercayaan antar entitas yang tidak saling mengenal di lingkungan digital.

    PKI bekerja melalui penerbitan sertifikat digital oleh Certificate Authority (CA), yaitu pihak tepercaya yang bertugas memverifikasi identitas pemilik kunci publik. Sertifikat digital berfungsi sebagai pengikat antara identitas pengguna dan kunci publiknya, sehingga pihak lain dapat memastikan bahwa kunci publik tersebut benar-benar milik entitas yang sah. Selain CA, PKI juga melibatkan komponen pendukung seperti Registration Authority (RA) untuk proses verifikasi identitas serta mekanisme pencabutan sertifikat melalui Certificate Revocation List (CRL) atau Online Certificate Status Protocol (OCSP).

    Penerapan PKI sangat luas dalam sistem keamanan informasi modern, seperti pada protokol HTTPS, tanda tangan digital, keamanan email, dan autentikasi pengguna. Keberadaan PKI memungkinkan terciptanya komunikasi yang aman dan terpercaya dalam skala besar, meskipun bergantung pada asumsi bahwa otoritas sertifikat menjalankan tugasnya secara benar dan aman. Oleh karena itu, PKI menjadi fondasi penting dalam infrastruktur keamanan digital yang digunakan saat ini.

## 3. Alat dan Bahan
    - Python 3.11
    - Visual Studio Code / editor lain  
    - Git dan akun GitHub  
    - Library cryptography pyopenssl

## 4. Langkah Percobaan
    1. Membuat Sertifikat Digital Sederhana
    2. Memverifikasi Sertifikat
    3. Analisis PKI

---

## 5. Source Code
    from cryptography import x509
    from cryptography.x509.oid import NameOID
    from cryptography.hazmat.primitives import hashes, serialization
    from cryptography.hazmat.primitives.asymmetric import rsa
    from datetime import datetime, timedelta

    # Generate key pair
    key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

    # Buat subject & issuer (CA sederhana = self-signed)
    subject = issuer = x509.Name([
        x509.NameAttribute(NameOID.COUNTRY_NAME, u"ID"),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"UPB Kriptografi"),
        x509.NameAttribute(NameOID.COMMON_NAME, u"example.com"),
    ])

    # Buat sertifikat
    cert = (
        x509.CertificateBuilder()
        .subject_name(subject)
        .issuer_name(issuer)
        .public_key(key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(datetime.utcnow())
        .not_valid_after(datetime.utcnow() + timedelta(days=365))
        .sign(key, hashes.SHA256())
    )

    # Simpan sertifikat
    with open("cert.pem", "wb") as f:
        f.write(cert.public_bytes(serialization.Encoding.PEM))

    print("Sertifikat digital berhasil dibuat: cert.pem")

## 6. Hasil dan Pembahasan
    Kode tersebut berhasil membuat sebuah sertifikat digital self-signed menggunakan konsep Public Key Infrastructure (PKI). Ketika program dijalankan, sistem akan menghasilkan sepasang kunci RSA (public key dan private key) dengan panjang 2048 bit, lalu membangun sertifikat digital yang ditandatangani oleh dirinya sendiri (issuer = subject). Output akhirnya adalah sebuah file cert.pem yang berisi sertifikat digital dalam format PEM

## 7. Jawaban Pertanyaan
    1. Certificate Authority (CA) berfungsi sebagai pihak tepercaya (trusted third party) yang:
        - Memverifikasi identitas entitas (server, organisasi, individu)
        - Menerbitkan sertifikat digital yang mengikat identitas dengan public key
        - Menandatangani sertifikat secara kriptografis
        - Menjadi akar kepercayaan (trust anchor) dalam sistem PKI 
    2. Alasan utama ketidakcukupan self-signed certificate: 
        a.Tidak ada validasi identitas eksternal
            - Sertifikat ditandatangani oleh dirinya sendiri
            - Tidak ada pihak tepercaya yang memverifikasi siapa pemiliknya
        b.Rentan terhadap serangan MITM
            - Penyerang bisa membuat sertifikat self-signed palsu
            - Klien tidak punya cara membedakan mana server asli
        c.Tidak dipercaya secara default
            - Browser dan OS tidak mempercayai self-signed certificate
            - Menimbulkan warning keamanan → trust is broken
        d. Tidak skalabel & tidak terkelola
            - Tidak ada revocation list (CRL) yang kredibel
            - Sulit mengelola rotasi sertifikat di sistem besar
    3. Mekanisme pencegahan MITM oleh PKI
        a. Rantai kepercayaan (Chain of Trust)
            - Sertifikat server ditandatangani oleh CA
            - Browser memverifikasi tanda tangan hingga ke Root CA terpercaya
            - Penyerang tidak bisa memalsukan tanda tangan CA
        b. Verifikasi identitas server
            - Domain (CN/SAN) di sertifikat harus cocok dengan URL
            - Sertifikat palsu untuk domain asli akan ditolak
        c. Kriptografi kunci publik + tanda tangan digital
            - CA menandatangani hash sertifikat dengan private key CA
            - Klien memverifikasi dengan public key CA
        d. Key exchange aman (TLS Handshake)
            - Setelah identitas server tervalidasi
            - Kunci sesi dibuat secara aman (ECDHE, dsb.)
            - Penyerang tidak bisa mendekripsi trafik meski menyadap

## 8. Kesimpulan
    Sertifikat yang dihasilkan cukup memadai untuk keperluan pembelajaran, simulasi, atau pengujian sistem internal. Namun, karena tidak melibatkan Certificate Authority tepercaya, sertifikat ini belum dapat menjamin kepercayaan publik dan kurang aman jika digunakan pada lingkungan produksi, terutama untuk mencegah risiko serangan man-in-the-middle dan masalah validasi identitas.

## 9. Daftar Pustaka
    - Stallings (2017), Bab 14.


## 10. Commit Log

commit : week10-pki
Author: Ahmad Nur Kholis <nurkholis.official05@gmail.com>
Date:   2026-01-16

    week10-pki
```
