import string

# key Menggunakan int
def caesar_encrypt(data, key):
    res = ""
    for x in range(len(data)):
        if data[x].isupper():
            pos = string.ascii_uppercase.index(data[x]) + key
            pos = pos % 26
            res += string.ascii_uppercase[pos]
        elif data[x].islower():
            pos = string.ascii_lowercase.index(data[x]) + key
            pos = pos % 26
            res += string.ascii_lowercase[pos]
        else:
            res += data[x]
    return res

def caesar_decrypt(data, key):
    res = ""
    for x in range(len(data)):
        if data[x].isupper():
            pos = string.ascii_uppercase.index(data[x]) - key
            pos = pos % 26
            res += string.ascii_uppercase[pos]
        elif data[x].islower():
            pos = string.ascii_lowercase.index(data[x]) - key
            pos = pos % 26
            res += string.ascii_lowercase[pos]
        else:
            res += data[x]
    return res

def main():
    enc = caesar_encrypt("RAVIDHARMAWAN", 17)
    print(enc)
    dec = caesar_decrypt(enc, 17)
    print(dec)

if __name__ == "__main__":
    main()