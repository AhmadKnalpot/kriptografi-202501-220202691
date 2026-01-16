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
