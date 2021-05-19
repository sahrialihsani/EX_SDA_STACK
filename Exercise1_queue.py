class Node : #Class Node
    def __init__(self,data=None,next_node=None):
        self.data = data
        self.next_node = next_node
    
    def get_data(self): #Dapatkan data
        return self.data
    
    #Tentukan ponter dan setter
    def get_next(self): #
        return self.next_node
    
    def set_next(self,new_node):
        self.next_node = new_node
        
class Queue : # Class Antrian
    def __init__(self,head=None):
        self.head = head
    #Metode antrian
    def enqueue(self,data):
        new_item = Node(data)
        current = self.head
        if current is None:
            self.head = new_item
        else:
            while current.get_next():
                current = current.get_next()
            current.set_next(new_item)
    #Metode Hapus Antrian
    def dequeue(self):
        current = self.head
        if current != None:
            self.head = current.get_next()
        else:
            print("Queue is empty.")

    def __len__(self):
        return len(self.temp)
    
    #Metode print antrian
    def print_queue(self):
        current = self.head
        self.temp = []
        while current:
            self.temp.append(current.get_data())
            current = current.get_next()
        print(self.temp)
    
# Inisiasi Objek Antrian
q = Queue()

q.enqueue("Data 1")
q.enqueue("Data 2")
q.enqueue("Data 3")
q.enqueue("Data 4")
q.enqueue("Data 5")

q.print_queue()

q.dequeue()
q.print_queue()

q.dequeue()
q.print_queue()

"""
Step: 
1. Buat Kelas node
Di kelas Node, kita akan mengatur data dan next_node (yaitu pointer) sama dengan None sebagai parameter dalam metode init sehingga jika kita tidak mengirim data dan pointer ke node berikutnya, ia akan mengembalikan None. Kemudian metode get_data dan get_next akan mengembalikan data dan node berikutnya masing-masing. Kami akan menambahkan metode lain set_next yang akan mengambil new_node sebagai parameter dan akan mengatur pointer dari Node sebelumnya menuju Node ini.

2. Buat Kelas Antrian
Setelah itu buat kelas lain bernama Queue, dan atur head (elemen 1st Queue) = None sebagai parameter dalam metode init. Kemudian kita akan memasukkan elemen pada Queue pertama menggunakan metode enqueue. Metode enqueue mengambil data sebagai parameter dan membuat Node menggunakannya. Sekarang, kami akan memeriksa apakah ada kepala di Antrian! Jika belum ada, kita setel elemen Node (new_item) / yang dibuat sebelumnya sebagai head. Jika sudah ada head yaitu ada elemen di Queue. Jadi, kita akan pergi ke akhir Queue menggunakan while loop dan ketika kita menemukan bahwa pointer dari node sebelumnya adalah null, kita mengatur pointer dari Node / elemen terakhir ke Node yang kita buat.

3. Menambahkan metode dequeque
Sekarang saatnya menambahkan metode dequeue untuk menghapus elemen pertama dari Queue. Pertama kita cek apakah Queue tersebut kosong atau tidak, jika tidak kosong maka kita setel elemen kedua Queue sebagai head dan elemen pertama (self.head) yang semula disimpan pada saat ini akan dihapus. Sekali lagi, jika Antrian kosong, kita cukup mencetak "Antrian kosong." .

"""


