import string

def create_alpha_key(data):
    data = data.lower() # kunci lama dijadikan bukan kapital seluruhnya
    key = "" # kunci yang baru dibuat string kosong

    for x in data: # setiap karakter di kunci lama dilooping
        if x not in key: # jika karakter di kunci lama tidak ada di kunci baru maka
            key += x # kunci baru menambahkan karakter kunci lama

    for x in string.ascii_lowercase: # setiap karakter di ascii_lowercase dilooping
        if x not in key: # jika karakter di ascii_lowercase tidak ada di kunci baru maka
            key += x # kunci baru menambahkan ke kunci baru

    return key # mengembalikkan nilai kunci baru ke enkripsi atau dekripsi

    # ----- Ilustrasi
    # create_alpha_key(data(cobo))
    # key = ""    
    # for x in data(cobo): -- Loop 4x

    # -- Loop 1
    #   if x("c") not in key(""):
    #       key += x(c)
    # -- Loop 2
    #   if x("o") not in key("c"):
    #       key += x("c" + "o")
    # -- Loop 3
    #   if x("b") not in key("co"):
    #       key += x("co" + "b")
    # -- Loop 4
    #   if x("o") not in key("cob"): -- Karena ada maka diskip
    
    # key = "coba"


def enkripsi(data, key):
    key = create_alpha_key(key) # ubah kunci pake fungsi create_alpha_key
    res = "" # res atau result atau hasil dibuat string kosong terlebih dahulu
    for x in range(len(data)):
        if data[x].islower():
            char = key[string.ascii_lowercase.index(data[x])]
            res += char
        elif data[x].isupper():
            char = key.upper()[string.ascii_uppercase.index(data[x])]
            res += char
        else:
            res += data[x]
    return res

def dekripsi(data, key):
    key = create_alpha_key(key)
    res = ""
    for x in range(len(data)):
        if data[x].islower():
            char = string.ascii_lowercase[key.index(data[x])]
            res += char
        elif data[x].isupper():
            char = string.ascii_uppercase[key.upper().index(data[x])]
            res += char
        else:
            res += data[x]
    return res

# Test 1
enc = enkripsi("WORKSHOPFIKTIKRIPTOGRAFI", "RAVIDHARMAWAN")
print(enc)
dec = dekripsi(enc, "RAVIDHARMAWAN")
print(dec)

# Test 2
enc = enkripsi("abcd", "cobo")
print(enc)
dec = dekripsi(enc, "cobo")
print(dec)