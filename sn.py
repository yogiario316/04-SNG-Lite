nama = ["Password maker by", "Yogi Ario"]
for i in nama:
    print(i)

print( )

import random
import string

def generate_random_password(length=7):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def custom_shift_password(user_input):
    def shift_char(c, shift):
        if c.isalpha():
            base = 'A' if c.isupper() else 'a'
            return chr((ord(c) - ord(base) + shift) % 26 + ord(base))
        elif c.isdigit():
            return chr((ord(c) - ord('0') + shift) % 10 + ord('0'))
        else:
            return c
    
    shifted_password = ''.join(shift_char(c, 6) for c in user_input)
    return shifted_password

def main():
    while True:
        print("Pilih opsi:")
        print("1. Buat Password secara random")
        print("2. Buat Password berdasarkan input custom dengan lompatan kelipatan 6")
        choice = input("Masukkan pilihan (1 atau 2): ")

        if choice == '1':
            length = int(input("Masukkan panjang minimal (minimal 7): "))
            if length < 7:
                print("Panjang minimal adalah 7. Menggunakan panjang 7.")
                length = 7
            password = generate_random_password(length)
        elif choice == '2':
            user_input = input("Masukkan Clue custom: ")
            password = custom_shift_password(user_input)
        else:
            print("Pilihan tidak valid.")
            continue

        print(f"Password yang dihasilkan: {password}")

        cont = input("Tekan 1 untuk lanjut membuat atau tekan sembarang tombol untuk keluar: ")
        if cont != '1':
            break

if __name__ == "__main__":
    main()
