def main():
    keys = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    shift = int(input("\nEnter Caesar Shift : "))
    plain = list(input("\nEnter the plain Text : "))
    cipher = ""

    if shift > 26:
        raise Exception("Only shift value below 26 accepted")

    tmp_lst = []

    for i in range(len(plain)):  # encryption => cipher = (plain + shift) mod 26
        # print(plain[i])
        try:
            pln_pos = keys.index(plain[i])
        except ValueError:
            tmp_lst.append(plain[i])
        else:
            # print(pln_pos)
            enc_pos = (pln_pos + shift) % 26
            # print(enc_pos)
            tmp_lst.append(keys[enc_pos])
            i += 1

    print(cipher.join(tmp_lst))

    # decryption => cipher = (plain + shift) mod 26


if __name__ == "__main__":
    main()
