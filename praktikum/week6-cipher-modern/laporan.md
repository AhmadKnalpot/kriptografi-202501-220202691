# Laporan Praktikum Kriptografi
Minggu ke-: 6
Topik: [Chiper modern]  
Nama: Ahmad Nur Kholis
NIM: 220202691
Kelas: 5 IKKA   


## 1. Tujuan
1. Mengimplementasikan algoritma DES untuk blok data sederhana.
2. Menerapkan algoritma AES dengan panjang kunci 128 bit.
3. Menjelaskan proses pembangkitan kunci publik dan privat pada algoritma RSA.

## 2. Dasar Teori
Cipher modern bertumpu pada dasar matematis yang kuat, biasanya melibatkan fungsi-fungsi non-linear, teori bilangan, serta operasi bit-level yang dirancang untuk menghasilkan confusion dan diffusion. Tidak seperti cipher klasik yang hanya memanipulasi huruf, cipher modern bekerja pada blok atau stream bit sehingga jauh lebih sulit dianalisis secara manual maupun dengan analisis frekuensi.

Dua kategori utama adalah kriptografi simetris dan asimetris. Simetris menggunakan satu kunci untuk enkripsi–dekripsi (misalnya AES), mengandalkan transformasi kompleks dan iteratif (rounds). Asimetris memakai pasangan kunci publik–privat (misalnya RSA, ECC), memanfaatkan masalah matematis yang dianggap sulit seperti faktorisasi bilangan besar atau logaritma diskrit.

Prinsip keamanan cipher modern mengikuti konsep security by design, yaitu asumsi bahwa penyerang mengetahui seluruh algoritma kecuali kunci. Keamanan diukur melalui computational hardness: selama usaha memecahkan kunci membutuhkan waktu dan komputasi yang tidak praktis, cipher dianggap aman. Pendekatan ini menjadikan cipher modern tahan terhadap analisis frekuensi, serangan linear–diferensial, dan mayoritas teknik klasik lainnya.

## 3. Alat dan Bahan
- Python 3.11 
- Visual Studio Code / editor lain  
- Git dan akun GitHub  

## 4. Langkah Percobaan
1. Implementasi DES (Opsional, Simulasi)
2. Implementasi AES-128
3. Implementasi RSA

## 5. Source Code
1. Implementasi DES (Opsional, Simulasi)

    from Crypto.Cipher import DES
    from Crypto.Random import get_random_bytes

    key = get_random_bytes(8)  # kunci 64 bit (8 byte)
    cipher = DES.new(key, DES.MODE_ECB)

    plaintext = b"ABCDEFGH"
    ciphertext = cipher.encrypt(plaintext)
    print("Ciphertext:", ciphertext)

    decipher = DES.new(key, DES.MODE_ECB)
    decrypted = decipher.decrypt(ciphertext)
    print("Decrypted:", decrypted)

2. Implementasi AES-128

    from Crypto.Cipher import AES
    from Crypto.Random import get_random_bytes

    key = get_random_bytes(16)  # 128 bit key
    cipher = AES.new(key, AES.MODE_EAX)

    plaintext = b"Modern Cipher AES Example"
    ciphertext, tag = cipher.encrypt_and_digest(plaintext)

    print("Ciphertext:", ciphertext)

    # Dekripsi
    cipher_dec = AES.new(key, AES.MODE_EAX, nonce=cipher.nonce)
    decrypted = cipher_dec.decrypt(ciphertext)
    print("Decrypted:", decrypted.decode())

3. Implementasi RSA

    from Crypto.PublicKey import RSA
    from Crypto.Cipher import PKCS1_OAEP

    # Generate key pair
    key = RSA.generate(2048)
    private_key = key
    public_key = key.publickey()

    # Enkripsi dengan public key
    cipher_rsa = PKCS1_OAEP.new(public_key)
    plaintext = b"RSA Example"
    ciphertext = cipher_rsa.encrypt(plaintext)
    print("Ciphertext:", ciphertext)

    # Dekripsi dengan private key
    decipher_rsa = PKCS1_OAEP.new(private_key)
    decrypted = decipher_rsa.decrypt(ciphertext)
    print("Decrypted:", decrypted.decode())

## 6. Hasil dan Pembahasan

## 7. Jawaban Pertanyaan
1. Perbedaan DES, AES, dan RSA (kunci & keamanan)
    DES dan AES adalah simetris, memakai satu kunci untuk enkripsi–dekripsi. DES hanya memiliki kunci 56-bit sehingga mudah dibobol, sedangkan AES memiliki kunci 128/192/256-bit dan jauh lebih aman. RSA bersifat asimetris dengan kunci publik–privat; keamanannya bergantung pada sulitnya memfaktorkan bilangan prima besar.
2. Karena DES terlalu kecil kuncinya dan dapat di-brute-force dalam waktu singkat. AES jauh lebih kuat, efisien, dan menjadi standar modern yang tahan terhadap serangan komputasi masa kini.
3. RSA disebut asimetris karena enkripsi dan dekripsi memakai kunci berbeda. Kuncinya dibuat dengan memilih dua prima besar p dan q, menghitung (n = pq), menentukan totien p(n), memilih e sebagai kunci publik, lalu menghitung d sebagai invers modular dari e untuk menjadi kunci privat
## 8. Kesimpulan
Cipher modern menuntut keamanan berbasis kompleksitas komputasi. DES melemah karena kunci pendek, AES menjadi standar karena memiliki struktur kuat dan ruang kunci besar, sementara RSA beroperasi dengan kunci publik–privat berbasis masalah faktorisasi bilangan besar. Dalam praktik modern, AES dipakai untuk enkripsi data dan RSA untuk pertukaran kunci karena sifat asimetrisnya.
## 9. Daftar Pustaka

- Stallings, W. *Cryptography and Network Security*.  

## 10. Commit Log

