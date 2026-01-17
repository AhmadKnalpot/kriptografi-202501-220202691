# Laporan Praktikum Kriptografi
Minggu ke-: 12
Topik: aplikasi tls
Nama: Ahmad Nur Kholis
NIM: 220202691
Kelas: 5 IKKA 

## 1. Tujuan
    1. Menganalisis penggunaan kriptografi pada email dan SSL/TLS.
    2. Menjelaskan enkripsi dalam transaksi e-commerce.
    3. Mengevaluasi isu etika & privasi dalam penggunaan kriptografi di kehidupan sehari-hari.

## 2. Dasar Teori
Transport Layer Security (TLS) merupakan protokol kriptografi yang dirancang untuk mengamankan komunikasi data pada jaringan komputer dengan menjamin kerahasiaan, integritas, dan autentikasi. TLS bekerja melalui mekanisme enkripsi data menggunakan kombinasi kriptografi asimetris dan simetris, di mana pertukaran kunci dilakukan secara aman pada tahap awal komunikasi (handshake), kemudian dilanjutkan dengan komunikasi terenkripsi menggunakan kunci sesi. Selain itu, TLS memanfaatkan sertifikat digital berbasis Public Key Infrastructure (PKI) untuk memverifikasi identitas server, sehingga mampu mencegah penyadapan data, pemalsuan identitas, dan serangan man-in-the-middle pada proses komunikasi.

E-commerce merupakan aktivitas transaksi bisnis yang dilakukan secara elektronik melalui internet dan melibatkan pertukaran data sensitif seperti informasi pengguna dan pembayaran. Karakteristik e-commerce yang beroperasi pada jaringan publik menjadikannya rentan terhadap berbagai ancaman keamanan, sehingga membutuhkan mekanisme perlindungan yang andal. Penerapan TLS pada aplikasi e-commerce, khususnya melalui protokol HTTPS, berperan penting dalam mengamankan proses login, transaksi, dan pertukaran data antara pengguna dan sistem. Dengan adanya TLS, keamanan komunikasi dapat terjaga sekaligus meningkatkan kepercayaan konsumen terhadap layanan e-commerce yang digunakan.

## 3. Alat dan Bahan  
- Visual Studio Code
- Git dan akun GitHub

## 4. Langkah Percobaan
1. Analisis SSL/TLS pada Email & Web
2. Studi Kasus E-commerce
3. Analisis Etika & Privasi

## 5. Source Code

## 6. Hasil dan Pembahasan
1. Studi kasus penerapan SSL/TLS
    a. E-commerce
        Pada platform e-commerce seperti Tokopedia dan Shopee, SSL/TLS diterapkan melalui protokol HTTPS untuk mengamankan komunikasi antara browser pengguna dan server aplikasi. Saat pengguna melakukan login, data kredensial dienkripsi menggunakan TLS sehingga tidak dapat disadap di jaringan publik. Pada proses pembayaran, TLS juga melindungi informasi sensitif seperti alamat, token pembayaran, dan OTP ketika berkomunikasi dengan payment gateway. Penerapan TLS ini memastikan kerahasiaan data, keutuhan transaksi, serta autentikasi server melalui sertifikat digital yang diterbitkan oleh Certificate Authority (CA) tepercaya.
    b. email
        TLS digunakan untuk mengamankan komunikasi antara client email dan mail server (SMTP, IMAP, POP3 over TLS). Selain itu, enkripsi end-to-end seperti PGP atau S/MIME digunakan untuk melindungi isi email agar hanya dapat dibaca oleh penerima yang sah. TLS melindungi jalur transmisi, sedangkan PGP/S-MIME melindungi konten, sehingga kombinasi keduanya memberikan lapisan keamanan berlapis dalam komunikasi email.
2. Analisis isu etika & privasi
    Penerapan TLS dan enkripsi email melindungi privasi dengan mencegah akses tidak sah terhadap isi komunikasi, namun menimbulkan dilema etika dan hukum terkait pengawasan dan penegakan aturan. Dekripsi email karyawan atau pemantauan komunikasi hanya dapat dibenarkan jika dilakukan secara transparan, proporsional, dan memiliki dasar hukum yang jelas, sementara pelemahan enkripsi oleh pemerintah berisiko merugikan keamanan publik. Tantangan utamanya adalah menyeimbangkan hak privasi individu dengan kepentingan keamanan bersama.

## 7. Jawaban Pertanyaan
1. Perbedaan utama antara HTTP dan HTTPS terletak pada keamanan komunikasi. HTTP mentransmisikan data dalam bentuk plaintext, sehingga informasi yang dikirim dapat dengan mudah disadap, dimodifikasi, atau dipalsukan oleh pihak ketiga di jaringan. Sebaliknya, HTTPS adalah HTTP yang berjalan di atas TLS, sehingga seluruh data dienkripsi, dijaga integritasnya, dan server diautentikasi melalui sertifikat digital. Asumsi mendasar HTTP adalah jaringan bersifat netral dan aman, sedangkan HTTPS dibangun atas asumsi realistis bahwa jaringan publik tidak dapat dipercaya. Oleh karena itu, HTTPS tidak hanya meningkatkan keamanan teknis, tetapi juga membangun kepercayaan pengguna dalam transaksi digital.
2. Sertifikat digital penting karena TLS tidak cukup hanya mengenkripsi data; sistem juga harus memastikan identitas pihak yang diajak berkomunikasi. Sertifikat digital, yang diterbitkan oleh Certificate Authority (CA), berfungsi sebagai bukti kriptografis bahwa suatu server benar-benar milik entitas yang diklaimnya. Tanpa sertifikat digital, enkripsi tetap dapat terjadi tetapi rentan terhadap serangan man-in-the-middle, di mana penyerang menyamar sebagai server yang sah. Dengan demikian, sertifikat digital menjadi fondasi kepercayaan dalam TLS karena menghubungkan kunci kriptografi dengan identitas legal atau organisasi tertentu.
3. Kriptografi mendukung privasi dengan memungkinkan individu dan organisasi berkomunikasi secara aman tanpa takut data mereka disadap atau dimanipulasi, yang merupakan prasyarat kebebasan berekspresi dan perlindungan data pribadi di era digital. Namun, kekuatan kriptografi ini juga menimbulkan dilema hukum dan etika, karena mekanisme yang sama dapat digunakan untuk menyembunyikan aktivitas ilegal dari penegak hukum. Tantangan utamanya terletak pada konflik antara hak atas privasi dan kepentingan keamanan publik, terutama dalam perdebatan mengenai akses pemerintah, backdoor enkripsi, dan pengawasan digital. Dengan demikian, kriptografi bukan hanya persoalan teknis, tetapi juga isu sosial, hukum, dan etika yang memerlukan keseimbangan kebijakan yang hati-hati.

## 8. Kesimpulan
TLS dan kriptografi merupakan fondasi keamanan komunikasi digital modern, khususnya pada e-commerce dan email. Namun, penerapannya tidak hanya menuntut keunggulan teknis, tetapi juga keseimbangan antara keamanan, privasi, etika, dan regulasi.

## 9. Daftar Pustaka
 - Stallings (2017), Bab 15.

## 10. Commit Log

commit : week12-aplikasi-tls
Author: Ahmad Nur Kholis <nurkholis.official05@gmail.com>
Date:   2026-01-17
