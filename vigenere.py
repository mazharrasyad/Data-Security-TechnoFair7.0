import string

def enkripsi(data, key):
    res = "" # result
    idx = 0 # index
    for x in range(len(data)):
        if data[x].isupper() or data[x].islower(): # termasuk alphabet besar atau kecil
            if data[x].islower():
                # 
                pos = (string.ascii_lowercase.index(data[x]) + string.ascii_lowercase.index(key.lower()[idx % len(key)])) % 26
                res += string.ascii_lowercase[pos]
            else:
                pos = (string.ascii_uppercase.index(data[x]) + string.ascii_uppercase.index(key.upper()[idx % len(key)])) % 26
                res += string.ascii_uppercase[pos]
            idx += 1
        else:
            res += data[x]
    return res

def dekripsi(data, key):
    res = ""
    idx = 0
    for x in range(len(data)):
        if data[x].isupper() or data[x].islower():
            if data[x].islower():
                pos = (string.ascii_lowercase.index(data[x])) - string.ascii_lowercase.index(key.lower()[idx % len(key)]) % 26
                res += string.ascii_lowercase[pos]
            else:
                pos = (string.ascii_uppercase.index(data[x])) - string.ascii_uppercase.index(key.upper()[idx % len(key)]) % 26
                res += string.ascii_uppercase[pos]
            idx += 1
        else:
            res += data[x]
    return res

# Test 1
enc = enkripsi("RAVID", "FIKTI")
print(enc)
dec = dekripsi(enc, "FIKTI")
print(dec)

# Test 2
enc = enkripsi("RAVI D", "FIKTI")
print(enc)
dec = dekripsi(enc, "FIKTI")
print(dec)