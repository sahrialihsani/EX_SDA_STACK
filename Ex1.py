class Stack :
    def __init__(self) :
        self.items = []
    def pushData(self, item) :
        self.items.append(item)
    def popData(self) :
        return self.items.pop()

# Insert data
dataStack = Stack()
#number 1-10
dataStack.pushData(1)
dataStack.pushData(2) 
dataStack.pushData(3) 
dataStack.pushData(4)

print("List Number 1-10: ",dataStack.items)
#Pop Data
print("Pop Data: ", dataStack.popData())

"""
Inisiasikan kelas beserta metode, 
metode : push dan pop
Stack merupakan bentuk lifo list, artinya last in first out, yang 
terakhir dimasukan, maka itu yang pertama kali keluar

1. Push data dalam hal ini saya menggunakan data berupa angka
2. Pop data, yang muncul adalah angka 4, karena stack menerapkan prinsip lifo, 4 merupakan
data terakhir yang dimasukan, maka 4 akan pertama kali keluar, jika ingin dihapus dari list

"""
