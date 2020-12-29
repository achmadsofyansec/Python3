import random 

karakter = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWQYZ1234567890-+=!@#$%^*"
panjang_pass = int(input("Panjang Karakter : "))
def pass_gen(num):
    password = ''
    for i in range(num):
        password += random.choice(karakter)
    return password
print(pass_gen(panjang_pass))