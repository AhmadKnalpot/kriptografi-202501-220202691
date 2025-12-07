# Laporan Praktikum Kriptografi
Minggu ke-: 5
Topik: [Chiper klasik]  
Nama: Ahmad Nur Kholis
NIM: 220202691
Kelas: 5 IKKA  

---

## 1. Tujuan
   1.  Menerapkan algoritma Caesar Cipher untuk enkripsi dan dekripsi teks.
   2.  Menerapkan algoritma Vigenère Cipher dengan variasi kunci.
   3.  Mengimplementasikan algoritma transposisi sederhana.
   4.  Menjelaskan kelemahan algoritma kriptografi klasik.

## 2. Dasar Teori
Cipher klasik adalah metode penyandian yang digunakan sebelum era komputer. Teknik ini bekerja dengan mengubah huruf, bukan menggunakan perhitungan matematika yang rumit. Ada dua cara utama dalam cipher klasik, yaitu substitusi dan transposisi. Dalam substitusi, huruf-huruf diganti dengan huruf lain, seperti pada metode Caesar, Vigenère, dan Playfair. Sementara itu, pada transposisi, posisi huruf diubah tanpa mengubah huruf itu sendiri, contohnya seperti Rail Fence dan Columnar Transposition. Metode ini dibuat agar pesan bisa tersembunyi, terutama ketika kemampuan untuk menganalisis pesan masih terbatas.

Namun, cipher klasik memiliki kelemahan.
Pola bahasa masih terlihat, sehingga mudah ditebak dengan menganalisis frekuensi huruf, terutama karena kunci yang digunakan pendek dan struktur teks tidak diubah secara menyeluruh. Keamanan dari metode ini bergantung pada penyembunyian cara kerjanya, bukan pada kekuatan kunci, sehingga tidak sesuai dengan standar kriptografi saat ini.

Meskipun sudah tidak aman, cipher klasik tetap penting karena menjadi dasar dari kriptografi modern.
Banyak konsep seperti kombinasi antara substitusi dan transposisi dalam algoritma blok berasal dari teknik klasik. Namun, teknik-teknik ini dikembangkan lebih lanjut dengan bantuan matematika, komputer, dan kunci yang lebih panjang.

## 3. Alat dan Bahan
(- Python 3.11
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan

1. Implementasi Caesar Cipher
2. Implementasi Vigenère Cipher
3. Implementasi Transposisi Sederhana 

---

## 5. Source Code

1. Implementasi Caesar Cipher

        def caesar_encrypt(plaintext, key):
    result = ""
    for char in plaintext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result

def caesar_decrypt(ciphertext, key):
    return caesar_encrypt(ciphertext, -key)

# Contoh uji
msg = "CLASSIC CIPHER"
key = 3
enc = caesar_encrypt(msg, key)
dec = caesar_decrypt(enc, key)
print("Plaintext :", msg)
print("Ciphertext:", enc)
print("Decrypted :", dec)

2. Implementasi Vigenère Cipher
def vigenere_encrypt(plaintext, key):
    result = []
    key = key.lower()
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 97
            base = 65 if char.isupper() else 97
            result.append(chr((ord(char) - base + shift) % 26 + base))
            key_index += 1
        else:
            result.append(char)
    return "".join(result)

def vigenere_decrypt(ciphertext, key):
    result = []
    key = key.lower()
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 97
            base = 65 if char.isupper() else 97
            result.append(chr((ord(char) - base - shift) % 26 + base))
            key_index += 1
        else:
            result.append(char)
    return "".join(result)

# Contoh uji
msg = "KRIPTOGRAFI"
key = "KEY"
enc = vigenere_encrypt(msg, key)
dec = vigenere_decrypt(enc, key)
print("Plaintext :", msg)
print("Ciphertext:", enc)
print("Decrypted :", dec)

3. Implementasi Transposisi Sederhana 
def transpose_encrypt(plaintext, key=5):
    ciphertext = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(plaintext):
            ciphertext[col] += plaintext[pointer]
            pointer += key
    return ''.join(ciphertext)

def transpose_decrypt(ciphertext, key=5):
    num_of_cols = int(len(ciphertext) / key + 0.9999)
    num_of_rows = key
    num_of_shaded_boxes = (num_of_cols * num_of_rows) - len(ciphertext)
    plaintext = [''] * num_of_cols
    col = 0
    row = 0
    for symbol in ciphertext:
        plaintext[col] += symbol
        col += 1
        if (col == num_of_cols) or (col == num_of_cols - 1 and row >= num_of_rows - num_of_shaded_boxes):
            col = 0
            row += 1
    return ''.join(plaintext)

# Contoh uji
msg = "TRANSPOSITIONCIPHER"
enc = transpose_encrypt(msg, key=5)
dec = transpose_decrypt(enc, key=5)
print("Plaintext :", msg)
print("Ciphertext:", enc)
print("Decrypted :", dec)

## 6. Hasil dan Pembahasan

## 7. Jawaban Pertanyaan
1. Caesar sangat lemah karena ruang kuncinya kecil dan pola gesernya sama di seluruh teks. Vigenere lebih kuat, tetapi jika kunci pendek atau berulang, pola periodiknya mudah dikenali dan tiap bagian bisa diperlakukan seperti Caesar Cipher.
2. Cipher klasik tidak menghilangkan pola statistik bahasa. Frekuensi huruf dan pola umum tetap muncul, sehingga penyerang bisa menebak huruf berdasarkan distribusi yang khas.
3. Substitusi mengganti huruf, tetapi tetap mempertahankan frekuensi bahasa jadi mudah dianalisis. Transposisi mengacak posisi huruf, tetapi distribusi huruf tetap sama jadi masih rentan jika pola pengacakan diketahui. Keduanya sederhana namun tidak aman secara modern.
## 8. Kesimpulan
cipher klasik tidak aman karena masih mempertahankan pola statistik bahasa, baik melalui penggantian huruf (substitusi) maupun pengacakan posisi (transposisi). Caesar Cipher terlalu sederhana dan mudah ditebak, sementara Vigenère Cipher pun dapat ditembus jika kuncinya pendek atau berulang. Keterbatasan ini membuat metode klasik rentan terhadap analisis frekuensi dan teknik kriptoanalisis dasar, sehingga tidak cocok untuk kebutuhan keamanan modern.

## 9. Daftar Pustaka
- Stallings (2017), Bab 3

## 10. Commit Log
