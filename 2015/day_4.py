import hashlib

INPUT_STRING = "yzbqklnj"

COUNTER = 0
while True:
    COUNTER += 1
    to_hash = f"{INPUT_STRING}{str(COUNTER)}"
    hash_hex = hashlib.md5(bytes(to_hash, 'utf-8'))
    hexdigest = hash_hex.hexdigest()
    if hexdigest[:6] == "000000":  # part 1 - 5 zeros ; part 2 - 6 zeros
        print(COUNTER)
        print(hexdigest)
        break
