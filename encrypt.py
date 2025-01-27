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

if __name__ == "__main__":
    file_path = "user128.txt"  
    byte_list = [] 
    try:
        with open(file_path, "rb") as file:
            while True:
                byte = file.read(1)  
                if not byte:  
                    break
                byte_list.append(byte)  
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
    byte_list = [int.from_bytes(i) for i in byte_list]
    key = input("Nhap Key: ")
    key = [ord(char) for char in key]
    byte_list += key
    ans = RC4(key, byte_list)
    hex_string = "".join(f"{num:02X}" for num in ans)
    try:
        with open("user128_en.md", "w", encoding="utf-8") as file:
            file.write(hex_string) 
        
        print(f"String has been written")
    except Exception as e:
        print(f"An error occurred: {e}")

