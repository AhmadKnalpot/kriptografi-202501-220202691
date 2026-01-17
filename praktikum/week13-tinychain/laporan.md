# Laporan Praktikum Kriptografi
Minggu ke-: 13
Topik: tinycoin
Nama: Ahmad Nur Kholis
NIM: 220202691
Kelas: 5 IKKA  

## 1. Tujuan
1. Menjelaskan peran hash function dalam blockchain.
2. Melakukan simulasi sederhana Proof of Work (PoW).
3. Menganalisis keamanan cryptocurrency berbasis kriptografi.

## 2. Dasar Teori
TinyChain merupakan model blockchain sederhana yang dirancang untuk menggambarkan prinsip dasar teknologi rantai blok, termasuk struktur blok, fungsi hash kriptografis, dan mekanisme konsensus. Dalam TinyChain, setiap blok berisi sekumpulan transaksi, hash blok sebelumnya, serta nilai nonce yang berfungsi sebagai variabel pencarian. Keterkaitan antarblok melalui hash menciptakan sifat immutability, di mana perubahan pada satu blok akan memengaruhi seluruh rantai setelahnya.

Proof of Work pada TinyChain berperan sebagai mekanisme konsensus untuk menentukan validitas blok baru. Proses ini mengharuskan node melakukan komputasi berulang guna menemukan nilai nonce yang menghasilkan hash sesuai dengan tingkat kesulitan tertentu, misalnya diawali dengan sejumlah nol. Secara teoretis, PoW memanfaatkan sifat satu arah fungsi hash: mudah diverifikasi tetapi sulit dihitung. Dengan demikian, penyerang akan menghadapi biaya komputasi yang tinggi jika ingin memodifikasi data historis.

Dalam kerangka teori sistem terdistribusi, TinyChain dengan PoW menunjukkan bagaimana keamanan blockchain dibangun dari kombinasi kriptografi dan insentif komputasi, bukan dari kepercayaan pada otoritas tunggal. Meskipun bersifat minimalis, TinyChain efektif sebagai representasi konseptual untuk memahami prinsip desentralisasi, toleransi terhadap serangan, serta trade-off antara keamanan, efisiensi, dan skalabilitas dalam desain blockchain.

## 3. Alat dan Bahan
- Python 3.1
- Visual Studio Code
- Git dan akun GitHub  

## 4. Langkah Percobaan
1. Membuat Struktur Blok
2. Membuat Blockchain
3. Analisis Proof of Work

## 5. Source Code
1. Blok
    import hashlib
    import time

    class Block:
    def __init__(self, index, previous_hash, data, timestamp=None):
        self.index = index
        self.timestamp = timestamp or time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.nonce)
        return hashlib.sha256(value.encode()).hexdigest()

    def mine_block(self, difficulty):
        while self.hash[:difficulty] != "0" * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(f"Block mined: {self.hash}")
2. Blockchain
    class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4

    def create_genesis_block(self):
        return Block(0, "0", "Genesis Block")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

        # Uji coba blockchain
        my_chain = Blockchain()
        print("Mining block 1...")
        my_chain.add_block(Block(1, "", "Transaksi A → B: 10 Coin"))

        print("Mining block 2...")
        my_chain.add_block(Block(2, "", "Transaksi B → C: 5 Coin"))
## 6. Hasil dan Pembahasan
1. pada kode <Block> yang sebelum diubah,output tidak muncul karena metode mine_block() tidak pernah dipanggil. Class hanyalah blueprint; tanpa instansiasi dan pemanggilan metode, tidak ada proses yang berjalan dan tidak ada output yang dicetak.

## 7. Jawaban Pertanyaan
1. Tanpa fungsi hash, blockchain hanyalah daftar data biasa. Hash menjadikannya struktur data yang aman secara kriptografis, bukan sekadar database terdistribusi.
2. PoW mencegah double spending bukan dengan larangan langsung, tetapi dengan membuat kecurangan menjadi tidak rasional secara ekonomi.
3. PoW kuat secara keamanan, tetapi lemah secara efisiensi energi, sehingga memicu lahirnya alternatif seperti Proof of Stake (PoS) yang mengalihkan keamanan dari energi ke kepemilikan aset.

## 8. Kesimpulan
Implementasi dasar blockchain dengan Proof of Work, di mana setiap blok ditambang menggunakan hash SHA-256 hingga memenuhi tingkat kesulitan tertentu. Proses ini memastikan integritas data melalui keterkaitan hash antarblok, sehingga cocok sebagai simulasi sederhana untuk konsep mining dan keamanan blockchain.

## 9. Daftar Pustaka
- Stallings (2017), Bab 16.
- Stinson (2019), Bab 8.


## 10. Commit Log

commit : week13-tintchain
Author: Ahmad Nur Kholis <nurkholis.official05@gmail.com>
Date:   2026-01-17
