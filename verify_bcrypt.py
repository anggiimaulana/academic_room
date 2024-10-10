import bcrypt

# Hash bcrypt yang ingin dicari password aslinya
hashed_password = b"$2y$10$zBh0rOkGJ3UCmdW9E45EkOneM.9ufGmIcguTiAueTlHWnIM7EklkC"

# Path ke file wordlist
wordlist_file = "wordlist.txt"

# Fungsi untuk brute-force bcrypt hash
def brute_force_bcrypt(hashed_password, wordlist_file):
    # Buka file wordlist
    with open(wordlist_file, 'r') as wordlist:
        # Coba setiap password dalam wordlist
        for word in wordlist:
            # Bersihkan kata dari spasi atau karakter newline
            word = word.strip()
            
            # Ubah kata menjadi bytes karena bcrypt membutuhkan input dalam bytes
            word_bytes = word.encode('utf-8')
            
            # Verifikasi hash bcrypt dengan password dari wordlist
            if bcrypt.checkpw(word_bytes, hashed_password):
                print(f"[+] Password ditemukan: {word}")
                return word  # Password ditemukan
            else:
                print(f"[-] Password {word} tidak cocok.")
    
    print("Password tidak ditemukan dalam wordlist.")
    return None

# Jalankan brute-force
brute_force_bcrypt(hashed_password, wordlist_file)
