class Queue :
  
    # Inisialisasi Object
    def __init__(self, c):
          
        self.queue = []
        self.front = self.rear = 0
        self.capacity = c
  
    # Fungsi masukan data
    def queueEnqueue(self, data):
  
        # cek antrian full atau tidak
        if(self.capacity == self.rear):
            print("\nQueue is full")
  
        # masukan elemen
        else:
            self.queue.append(data)
            self.rear += 1
  
    # Fungsi menghapus data dan elemen pada antrian
    def queueDequeue(self):
  
        # jika antrian tidak ada data disana
        if(self.front == self.rear):
            print("Queue is empty")
  
        # Jika ada hapus elemen sesuai prinsip fifo pada antrian
        else:
            x = self.queue.pop(0)
            self.rear -= 1
  
    # Fungsi tampilkan hasil antrian
    def queueDisplay(self):
          
        if(self.front == self.rear):
            print("\nQueue is Empty")
  
        # tampilkan semua elemen pada antrian
        for i in self.queue:
            print(i, "<--", end = '')
      
    # Tampilkan elemen awal pada antrian
    def queueFront(self):
          
        if(self.front == self.rear):
            print("\nQueue is Empty")
  
        print("\nFront Element is:", 
              self.queue[self.front])
  
if __name__=='__main__':
  
    #Tentukan kapasitas data pada antrian, contoh 4
    q = Queue(4)
  
    # cetak antrian
    q.queueDisplay()
  
    # Masukan data pada elemen antrian
    q.queueEnqueue(50)
    q.queueEnqueue(60)
    q.queueEnqueue(70)
    q.queueEnqueue(80)
  
    # cetak antrian sekarang
    q.queueDisplay()
  
    # Lakukan insert data lagi, apakah masih bisa atau tidak
    q.queueEnqueue(90)
  
    # cetak antrian
    q.queueDisplay()
  
    #Hapus elemen pada antrian (using fifo)
    q.queueDequeue()
    q.queueDequeue()
    q.queueDequeue()

    print("\n\nSetelah 3 elemen dihapus\n")
  
    # cetak elemen antrian
    q.queueDisplay()
  
    #cetak elemen paling depan pada antrian
    q.queueFront()
