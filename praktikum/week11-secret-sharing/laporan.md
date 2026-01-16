# Laporan Praktikum Kriptografi
Minggu ke-: 11 
Topik: secret-sharing 
Nama: Ahmad Nur Kholis
NIM: 220202691
Kelas: 5 IKKA   

## 1. Tujuan
    1.Menjelaskan konsep Shamir Secret Sharing (SSS).
    2.Melakukan simulasi pembagian rahasia ke beberapa pihak menggunakan skema SSS.
    3.Menganalisis keamanan skema distribusi rahasia.

## 2. Dasar Teori
    Secret sharing adalah teknik kriptografi yang digunakan untuk membagi sebuah rahasia (secret) menjadi beberapa bagian yang disebut share, sehingga rahasia tersebut hanya dapat direkonstruksi jika sejumlah minimal bagian tertentu digabungkan kembali. Konsep ini dirancang untuk menghindari ketergantungan pada satu pihak atau satu titik kegagalan (single point of failure). Dengan secret sharing, tidak ada satu pihak pun yang memegang rahasia secara utuh, sehingga keamanan dan keandalan sistem meningkat.

    Skema secret sharing yang paling terkenal adalah Shamir’s Secret Sharing (SSS). Dalam skema ini, sebuah rahasia direpresentasikan sebagai konstanta dari suatu polinom berderajat t-1, t adalah ambang batas (threshold). Nilai polinom tersebut kemudian dihitung pada beberapa titik berbeda untuk menghasilkan share. Sifat matematis polinom menjamin bahwa minimal t share diperlukan untuk merekonstruksi rahasia, sementara jumlah share yang lebih sedikit tidak memberikan informasi apa pun tentang rahasia tersebut.

    Secret sharing banyak diterapkan pada sistem keamanan modern, seperti manajemen kunci kriptografi, sistem escrow, blockchain, dan pengamanan data sensitif pada organisasi terdistribusi. Dengan pendekatan ini, kepercayaan tidak terpusat pada satu entitas, melainkan didistribusikan ke beberapa pihak, sehingga risiko kebocoran, penyalahgunaan, atau kehilangan rahasia dapat diminimalkan secara signifikan.

## 3. Alat dan Bahan
- Python 3.11
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library secretsharing
## 4. Langkah Percobaan
    1.Implementasi Shamir Secret Sharing
    2.Simulasi Manual (Tanpa Library)
    3.Analisis Keamanan

## 5. Source Code
    import random

    # Bilangan prima besar (digunakan sebagai modulo)
    PRIME = 208351617316091241234326746312124448251235562226470491514186331217050270460481

    # FUNGSI SPLIT SECRET
    def split_secret(secret_int, t, n):
        # Buat koefisien polinomial (derajat t-1)
        coeffs = [secret_int] + [random.randrange(1, PRIME) for _ in range(t - 1)]
        shares = []

        for x in range(1, n + 1):
            y = 0
            for i in range(len(coeffs)):
                y += coeffs[i] * pow(x, i, PRIME)
            y %= PRIME
            shares.append((x, y))

        return shares

    # FUNGSI REKONSTRUKSI SECRET
    def recover_secret(shares):
        secret = 0

        for j, (xj, yj) in enumerate(shares):
            numerator = 1
            denominator = 1

            for i, (xi, _) in enumerate(shares):
                if i != j:
                    numerator = (numerator * (-xi)) % PRIME
                    denominator = (denominator * (xj - xi)) % PRIME

            lagrange = numerator * pow(denominator, -1, PRIME)
            secret = (secret + yj * lagrange) % PRIME

        return secret

    # PROGRAM UTAMA

    # Rahasia (string → hex → integer)
    secret = "KriptografiUPB2025"
    secret_hex = secret.encode().hex()
    secret_int = int(secret_hex, 16)

    # Split secret (threshold 3 dari 5)
    shares = split_secret(secret_int, t=3, n=5)
    print("Shares:")
    for s in shares:
        print(s)

    # Rekonstruksi secret dari 3 share
    recovered_int = recover_secret(shares[:3])
    recovered_hex = hex(recovered_int)[2:]
    recovered_secret = bytes.fromhex(recovered_hex).decode()

    print("\nRecovered secret:", recovered_secret)


## 6. Hasil dan Pembahasan
    - ada terdapat error pada library <secretsharing>, karena itu hanya bisa dijalankan di ditipe python 2. 
    - sehingga saya ganti dengan library yang komplatible yaitu <Shamir Secret Sharing>
## 7. Jawaban Pertanyaan
    1. 
    Keuntungan utama SSS adalah tidak ada satu pihak pun yang memegang rahasia secara utuh. Pada pembagian salinan kunci langsung, kebocoran pada satu pihak saja sudah cukup untuk membocorkan seluruh rahasia. Sebaliknya, dalam SSS, setiap pihak hanya memegang share yang tidak memiliki makna apa pun secara individual. Rahasia baru bisa direkonstruksi jika sejumlah share minimum digabungkan, sehingga risiko kebocoran, pencurian, atau penyalahgunaan kunci dapat ditekan secara signifikan.
    2.
    Threshold k menentukan tingkat toleransi dan keamanan sistem. Nilai k menyatakan jumlah minimal share yang dibutuhkan untuk merekonstruksi rahasia. Jika jumlah share yang tersedia kurang dari k, maka secara matematis tidak ada informasi tentang rahasia yang dapat diperoleh. Dengan demikian, semakin besar nilai k, semakin tinggi tingkat keamanannya, tetapi juga semakin rendah fleksibilitas. Threshold ini memungkinkan perancangan sistem yang seimbang antara keamanan, keandalan, dan ketersediaan.
    3.
    Salah satu contoh nyata penggunaan SSS adalah pengelolaan kunci master pada sistem keuangan atau pusat data organisasi. Misalnya, kunci enkripsi utama disimpan menggunakan skema 3-dari-5, di mana lima pejabat berbeda masing-masing memegang satu share. Kunci hanya dapat direkonstruksi jika minimal tiga pejabat hadir dan menyetujui akses. Skema ini mencegah penyalahgunaan oleh satu orang, sekaligus tetap memungkinkan pemulihan kunci jika sebagian pihak tidak tersedia.

## 8. Kesimpulan
Hasil eksekusi menunjukkan bahwa rahasia dapat dipulihkan secara utuh menggunakan tiga share pertama, membuktikan bahwa mekanisme interpolasi Lagrange bekerja dengan benar. Secara keseluruhan, program ini menunjukkan bahwa Shamir Secret Sharing mampu meningkatkan keamanan penyimpanan rahasia dengan menghindari single point of failure, sekaligus tetap memberikan fleksibilitas dan keandalan dalam pengelolaan informasi sensitif dan diperlukannya jeli dalam pemilihan versi python, karena ada beberapa variable yang sudah tidak digunakan pada versi yang terbaru.

## 9. Daftar Pustaka
    - Stinson (2019), Bab 6.

## 10. Commit Log
commit : week11-secret-sharing
Author: Ahmad Nur Kholis <nurkholis.official05@gmail.com>
Date:   2026-01-16

