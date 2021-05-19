
#Rekursif Binary Search 
def binary_search(array, kiri, kanan, nilaidicari):
 
    # cek base
    if kanan >= kiri:
 
        tengah = (kanan + kiri) // 2
 
        # Jika elemen ada di tengah
        if array[tengah] == nilaidicari:
            return tengah
 
        # Jika elemen lebih kiri dari tengah, elemen berada di sebelah kiri
        elif array[tengah] > nilaidicari:
            return binary_search(array, kiri, tengah - 1, nilaidicari)
 
        # Jika tidak, elemen hanya bisa ada di sebelah kanan
        else:
            return binary_search(array, tengah + 1, kanan, nilaidicari)
 
    else:
        # Elemen tidak ada di array
        return -1
 
# Masukan data pada berbentuk array
array = [ 10, 20, 30, 40, 50, 60 ]
nilaidicari = 40
# Lakukan pencarian
result = binary_search(array, 0, len(array)-1, nilaidicari)
if result != -1:
    print("Elemen berada pada indeks ke: ", str(result))
else:
    print("Elemen tidak berada didalam array")
