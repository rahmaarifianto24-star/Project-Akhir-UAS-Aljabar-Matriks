import rahma123 as aljabar

while True:
    print("\n=== PROGRAM ALJABAR MATRIKS ===")
    print("1. Perkalian Skalar")
    print("2. Penjumlahan Matriks")
    print("3. Transpose Matriks")
    print("4. Keluar")

    pilihan = int(input("Masukkan pilihan: "))

    if pilihan == 1:
        print("\nMasukkan Matriks 2x2")
        A = []

        for i in range(2):
            baris = list(map(int, input(f"Baris {i+1}: ").split()))
            A.append(baris)

        skalar = int(input("Masukkan nilai skalar: "))

        print("\nHasil Perkalian Skalar:")
        print(aljabar.perkalian_skalar(A, skalar))

    elif pilihan == 2:
        print("\nMasukkan Matriks A")
        A = []

        for i in range(2):
            baris = list(map(int, input(f"Baris {i+1}: ").split()))
            A.append(baris)

        print("\nMasukkan Matriks B")
        B = []

        for i in range(2):
            baris = list(map(int, input(f"Baris {i+1}: ").split()))
            B.append(baris)

        print("\nHasil Penjumlahan:")
        print(aljabar.penjumlahan_matriks(A, B))

    elif pilihan == 3:
        print("\nMasukkan Matriks")
        A = []

        for i in range(2):
            baris = list(map(int, input(f"Baris {i+1}: ").split()))
            A.append(baris)

        print("\nHasil Transpose:")
        print(aljabar.transpose(A))

    elif pilihan == 4:
        print("\nProgram selesai. Terima kasih.")
        break

    else:
        print("\nPilihan tidak valid!")