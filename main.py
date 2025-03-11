def izin():
    izin_girisi = input("İzinleri giriniz (örn: rwxrwxrwx): ").strip()

    for i in range(0, len(izin_girisi), 3):
        grup = izin_girisi[i:i + 3]
        toplam = 0

        if 'r' in grup:
            toplam += 4
        if 'w' in grup:
            toplam += 2
        if 'x' in grup:
            toplam += 1

        print(toplam, end=" ")

izin()