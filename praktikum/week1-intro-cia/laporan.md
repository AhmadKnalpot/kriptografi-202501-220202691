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
Sejarah Kriptografi & Prinsip CIA

Kriptografi berasal dari kata Yunani kryptos (rahasia) dan graphein (menulis), yang berarti seni menulis pesan rahasia. Sejak zaman kuno, seperti sandi Caesar di Romawi dan sandi substitusi pada abad pertengahan, kriptografi digunakan untuk menjaga kerahasiaan pesan militer. Perkembangannya terus berlanjut hingga era komputer modern dengan munculnya algoritma seperti DES, RSA, dan AES. Dalam keamanan informasi, kriptografi berperan penting untuk menjaga prinsip CIA, yaitu Confidentiality (kerahasiaan data), Integrity (keutuhan data), dan Availability (ketersediaan sistem). Ketiga prinsip ini menjadi dasar dalam merancang sistem keamanan digital yang andal dan terpercaya.

A. Era Kriptografi Klasik

    Era kriptografi klasik dimulai sejak ribuan tahun lalu, jauh sebelum munculnya komputer. Pada masa ini, teknik kriptografi dilakukan secara manual menggunakan operasi sederhana pada huruf atau simbol. Tujuannya adalah menyembunyikan makna pesan agar hanya penerima yang berhak dapat membacanya.

    Contoh paling terkenal adalah sandi Caesar yang digunakan oleh Julius Caesar di Romawi kuno dengan cara menggeser huruf-huruf alfabet sejauh beberapa posisi. Selain itu, dikenal juga sandi substitusi (mengganti setiap huruf dengan huruf lain) dan sandi transposisi (menyusun ulang urutan huruf).

    Ciri utama kriptografi klasik adalah berbasis huruf alfabet dan pola bahasa, bukan bilangan biner seperti pada sistem modern. Meskipun sederhana, konsep dasarnya menjadi fondasi bagi perkembangan algoritma kriptografi modern yang lebih kompleks dan berbasis matematika.

B. Perkembangan Kriptografi Modern

    Kriptografi modern mulai berkembang pesat pada abad ke-20, seiring kemunculan komputer dan kebutuhan keamanan data dalam komunikasi digital. Berbeda dari kriptografi klasik yang berbasis huruf, kriptografi modern menggunakan teori matematika, logika, dan komputasi untuk melindungi informasi.

    Perkembangan ini dimulai dengan kriptografi simetris, seperti DES (Data Encryption Standard) pada tahun 1970-an, di mana pengirim dan penerima menggunakan kunci yang sama. Selanjutnya muncul kriptografi asimetris, yang diperkenalkan melalui algoritma RSA (Rivest–Shamir–Adleman) pada tahun 1977, menggunakan pasangan kunci publik dan privat.

    Di era digital saat ini, kriptografi modern mendukung banyak aspek keamanan seperti SSL/TLS untuk komunikasi internet, blockchain, tanda tangan digital, dan kriptografi kuantum. Dengan terus berkembangnya teknologi dan ancaman siber, kriptografi modern menjadi tulang punggung utama dalam menjaga kerahasiaan, integritas, dan keaslian data di dunia digital.
 C. Evolusi Menuju Kriptografi Kontemporer

    Evolusi menuju kriptografi kontemporer terjadi sebagai respons terhadap meningkatnya kompleksitas teknologi dan ancaman keamanan digital. Setelah era kriptografi modern yang didominasi oleh algoritma seperti DES, AES, dan RSA, kebutuhan akan sistem yang lebih aman, efisien, dan tahan terhadap serangan komputasi canggih menjadi semakin mendesak.

    Perkembangan ini melahirkan konsep baru seperti kriptografi eliptik (Elliptic Curve Cryptography / ECC) yang menawarkan keamanan tinggi dengan ukuran kunci lebih kecil, serta kriptografi berbasis hash yang digunakan dalam blockchain dan cryptocurrency. Selain itu, muncul pula riset dalam kriptografi pasca-kuantum (Post-Quantum Cryptography) untuk menghadapi potensi ancaman dari komputer kuantum yang dapat memecahkan algoritma klasik seperti RSA.

    Kriptografi kontemporer tidak hanya berfokus pada enkripsi, tetapi juga pada privasi, autentikasi, dan keandalan sistem digital secara menyeluruh, menjadikannya fondasi utama dalam keamanan informasi di era teknologi modern dan masa depan.

1. Confidentiality (Kerahasiaan)

Penjelasan:
Menjamin bahwa data hanya dapat diakses oleh pihak yang berwenang. Tujuannya adalah mencegah kebocoran atau akses tidak sah terhadap informasi sensitif.

Contoh:

    - Data login pengguna (username dan password) disimpan dalam bentuk terenkripsi.

    - Pesan di WhatsApp dienkripsi end-to-end, sehingga hanya pengirim dan penerima yang bisa membacanya.

    - Dokumen perusahaan dilindungi dengan password agar tidak bisa dibuka oleh orang lain.

2. Integrity (Keutuhan)

Penjelasan:
Menjaga agar data tetap asli, akurat, dan tidak diubah tanpa izin. Artinya, data yang diterima harus sama persis dengan yang dikirim.

Contoh:

    - Penggunaan checksum atau hash (misalnya SHA-256) untuk memastikan file tidak rusak atau diubah saat dikirim.

    - Tanda tangan digital digunakan untuk menjamin bahwa dokumen elektronik tidak dimodifikasi setelah disetujui.

    - Dalam transaksi bank online, sistem memastikan nominal transfer tidak dapat diubah di tengah proses.

3. Availability (Ketersediaan)

Penjelasan:
Menjamin sistem, data, dan layanan selalu tersedia kapan pun dibutuhkan oleh pengguna yang sah. Gangguan seperti serangan, kerusakan, atau overload harus diminimalkan.

Contoh:

   - Server website menggunakan backup dan load balancing agar tetap online meskipun salah satu server mati.

    - Sistem perbankan memiliki disaster recovery plan agar tetap beroperasi saat terjadi gangguan.

    - Penggunaan UPS atau generator cadangan untuk memastikan layanan tetap aktif saat listrik padam.

Quizz 

1. Siapa tokoh yang dianggap sebagai Bapak Kriptografi Modern?

Tokoh yang dianggap sebagai Bapak Kriptografi Modern adalah Whitfield Diffie dan Martin Hellman.
Mereka memperkenalkan konsep kriptografi kunci publik (public-key cryptography) pada tahun 1976, yang menjadi dasar bagi banyak sistem keamanan digital saat ini, termasuk RSA dan SSL/TLS.
2. Sebutkan algoritma kunci publik yang populer digunakan saat ini

Beberapa algoritma kunci publik yang populer dan banyak digunakan adalah:

    - RSA (Rivest–Shamir–Adleman) – digunakan dalam enkripsi dan tanda tangan digital.

    - Diffie-Hellman – digunakan untuk pertukaran kunci secara aman.

    - ECC (Elliptic Curve Cryptography) – menawarkan keamanan tinggi dengan ukuran kunci yang lebih kecil.

    - ElGamal – digunakan dalam sistem tanda tangan digital dan enkripsi asimetris.
3. Perbedaan Utama antara Kriptografi Klasik dan Kriptografi Modern

Kriptografi klasik menggunakan teknik sederhana berbasis huruf dan simbol, seperti sandi substitusi dan transposisi, untuk menyembunyikan pesan. Proses enkripsi dan dekripsi biasanya dilakukan secara manual atau dengan alat mekanis seperti mesin Enigma. Sistem ini umumnya menggunakan satu kunci yang sama (simetris) untuk mengenkripsi dan mendekripsi pesan, sehingga relatif mudah dipecahkan dengan analisis frekuensi atau pola bahasa.

Sebaliknya, kriptografi modern berbasis pada prinsip matematika dan teori komputasi. Prosesnya menggunakan bilangan biner dan algoritma kompleks seperti RSA, AES, atau Elliptic Curve Cryptography (ECC). Selain kunci simetris, kriptografi modern juga memperkenalkan konsep kunci asimetris, yaitu pasangan kunci publik dan privat. Dengan bantuan komputer, kriptografi modern mampu memberikan tingkat keamanan yang jauh lebih tinggi dan menjadi dasar utama dalam melindungi komunikasi digital di era teknologi saat ini.
