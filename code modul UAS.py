import rahma123 as modul 

def perkalian_skalar(matriks, skalar):
    hasil = []

    for baris in matriks:
        hasil_baris = []

        for elemen in baris:
            hasil_baris.append(elemen * skalar)

        hasil.append(hasil_baris)

    return hasil


def penjumlahan_matriks(A, B):
    hasil = []

    for i in range(len(A)):
        baris = []

        for j in range(len(A[0])):
            baris.append(A[i][j] + B[i][j])

        hasil.append(baris)

    return hasil

def transpose(A):
    hasil = []

    for j in range(len(A[0])):
        baris = []

        for i in range(len(A)):
            baris.append(A[i][j])

        hasil.append(baris)

    return hasil

