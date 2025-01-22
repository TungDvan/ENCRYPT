def RC4(key, cipher):
    map = [i for i in range(256)]
    ans = []
    tmp1 = 0
    for i in range(256):
        tmp1 = (tmp1 + map[i] + key[i % len(key)]) & 0xFF
        map[i], map[tmp1] = map[tmp1], map[i]
    tmp1, tmp2 = 0, 0
    for i in range(len(cipher)):
        tmp1 = (tmp1 + 1) & 0xFF
        tmp2 = (tmp2 + map[tmp1]) & 0xFF
        map[tmp1], map[tmp2] = map[tmp2], map[tmp1]
        ans.append(cipher[i] ^ map[(map[tmp1] + map[tmp2]) & 0xFF])
    return ans

key = input("Nhap Key: ")
key = [ord(char) for char in key]

try:
    with open('user128_en.md', "r", encoding="utf-8") as file:
        read_string = file.read()  # Read the content of the file
except Exception as e:
    print(f"An error occurred while reading: {e}")

cipher = list(bytes.fromhex(read_string))

cipher = RC4(key, cipher)
for i in cipher: print(end = chr(i))