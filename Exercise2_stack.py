class Palindrome() :
     def __init__(self) :
        self.items = []
     def emptyData(self) :
        return self.items == []
     def pushData(self, item) :
        self.items.append(item)
     def popData(self) :
        return self.items.pop()
     def sizeData(self) :
        return len(self.items)

dataStack = Palindrome()
#Cek Inputan
text = input('Enter the string: ')

for char in text :
    dataStack.pushData(char)

#string tidak ada yg kosong
text_reverse = ''
while not dataStack.emptyData():
    text_reverse = text_reverse + dataStack.popData()

#condition
if text == text_reverse:
    print('String is a palindrome') # string as a palindrome
else :
    print('String is not a palindrome') #String not as a palindrome

    
"""
Step by step: 
Kelas bernama 'Palindrome' didefinisikan dengan metode 'init'.

Metode ini menginisialisasi daftar kosong.

Metode lain bernama 'emptyData' didefinisikan bahwa memeriksa apakah tumpukan kosong atau tidak.

Metode lain bernama 'pushData' didefinisikan yang menambahkan elemen ke stack.

Metode lain bernama 'popData' didefinisikan yang menghapus elemen dari tumpukan.

Contoh 'Palindrome' ini didefinisikan.

String diambil dari pengguna.

Ini berulang-ulang, dan metode 'emptyData' dipanggil di atasnya.

String kosong lainnya didefinisikan, dan string dibalik.

String terbalik ini disimpan dalam string kosong.

String terbalik ini dan string dari pengguna dibandingkan.

Jika mereka sama, itu berarti itu adalah palindrome.

Jika tidak, itu bukan palindrome.

Output yang relevan ditampilkan pada konsol.
"""
