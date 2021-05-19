if __name__=="__main__":    
    print("Здравствуйте, что желаете сделать?")
    print("Выберите режим работы программы")
    print("1 - шифрование")
    print("2 - расшифровывание")
    mode = int(input("Выберите режим работы: "))
    print("Выберите алгоритм боты программы")
    print("1 - цезарь")
    print("2 - виженер")
    algo = int(input("Выберите алгоритм работы: "))
    word = input("Введите слово: ")
    key = input("Введите ключ: ")
    get_base = lambda letter: ord('A') if letter >='A' and letter <='Z' else ord('a')
    cezar_encryption = lambda letter: chr(get_base(letter) + ((ord(letter) - get_base(letter) + int(key)) % 26))
    cezar_decryption = lambda letter: chr(get_base(letter) + ((ord(letter) - get_base(letter) - int(key) + 26) % 26))
    vizener_encryption = lambda letter: chr(get_base(letter[0]) + ((ord(letter[0]) - get_base(letter[0]) + ord(letter[1]) - get_base(letter[1])) % 26))
    vizener_decryption = lambda letter: chr(get_base(letter[0]) + ((ord(letter[0]) - get_base(letter[0]) - ord(letter[1]) + get_base(letter[1]) + 26) % 26))
    if (algo == 1 and mode == 1):
        f = cezar_encryption
        print(''.join(list(map(f, word))))
    if (algo == 1 and mode == 2):
        f = cezar_decryption
        print(''.join(list(map(f, word))))

    if (algo == 2):
        if (len(word) < len(key)):
            raise ValueError("key > word")
        if not all(c.isupper() for c in word):
            raise ValueError("word contains negative symbols")
        if not all(c.isupper() for c in key):
            raise ValueError("key contains negative symbols")
        s = key
        i = 0
        while(len(key) < len(word)):
            key += s[i]
            i+=1
            if i>=len(s):
                i = 0
        print(f"Modified key: {key}")
        if (mode == 1):
            f = vizener_encryption
            print(''.join(list(map(f, zip(word, key)))))
        if (mode == 2):
            f = vizener_decryption
            print(''.join(list(map(f, zip(word, key)))))