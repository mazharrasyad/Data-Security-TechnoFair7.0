import base64
# dijalankan dibukan python3

def xor_encrypt(data, key):
    res = ""
    for x in range(len(data)):
        # ord = bilangan ascii
        # ^ = xor
        res += chr(ord(data[x]) ^ ord(key[x % len(key)]))
    return base64.b64encode(res)

def xor_decrypt(data, key):
    data = base64.b64decode(data)
    res = ""
    for x in range(len(data)):
        res += chr(ord(data[x]) ^ ord(key[x % len(key)]))
    return res

def main():
    enc = xor_encrypt("RAVIDHARMAWAN", "FIKTIA")
    print(enc)
    dec = xor_decrypt(enc, "FIKTIA")
    print(dec)

if __name__ == "__main__":
    main()