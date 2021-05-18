#Infix to postfix
class convertToPost:
    precedence={'^':5,'*':4,'/':4,'+':3,'-':3,'(':2,')':1}
    def __init__(self):
        self.items=[]
        self.size=-1
    def pushData(self,value):
        self.items.append(value)
        self.size+=1
    def popData(self):
        if self.empty():
            return 0
        else:
            self.size-=1
            return self.items.popData()
    def empty(self):
        if(self.size==-1):
            return True
        else:
            return False
    def see(self):
        if self.empty():
            return false
        else:
            return self.items[self.size]
    def isOperand(self,i):
        if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ': #Cek condition all alphaphet was true
            return True
        else:
            return False
    def convert (self,expr):
        postfix=""
        print('postfix expression after every iteration is:')
        for i in expr:
            if(len(expr)%2==0):
                print("Incorrect infix expression")
                return False
            elif(self.isOperand(i)):
                postfix +=i
            elif(i in '+-*/^'):
                while(len(self.items)and self.precedence[i]<=self.precedence[self.see()]):
                    postfix+=self.popData()
                self.pushData(i)
            elif i == '(':
                self.pushData(i)
            elif i == ')':
                o=self.popData()
                while o!='(':
                    postfix +=o
                    o=self.popData()
            print(postfix)
                #end of for
        while len(self.items):
            if(self.see()=='('):
                self.popData()
            else:
                postfix+=self.popData()
        return postfix
s=convertToPost()
expr=input('Enter expression: ')
result=s.convert(expr)
if (result!=False):
    print("Postfix of :",expr,"is = ",result)

    
"""
Step by step 
1.	Ekspresi ditulis dalam bentuk string


2.	For i in expr:
    If i is alphabet or digit:
        tambahkan ke postfix
    Else if i == '(':
        masukan '(' kedalam stack
    Else if i == ')':
        Pop elemen dari tumpukan dan tambahkan ekspresi postfix sampai kita mendapatkan ')' di atas tumpukan.
        Pop '(' dari tumpukan dan jangan tambahkan dalam ekspresi postfix.
    Else if i == in '*/+-‘:
        If stack is empty or top of the stack is '(':
           masukan operator kedalam stack/ tumpukan data
        Else:
            Pop elemen dari tumpukan dan lanjutkan ini sampai operator di bagian atas tumpukan memiliki tempat tinggal yang sama atau kurang maka i.
    Else:
       masukan i kedalam stack


3. Setelah  memindai ekpresi sepenuhnya, mulailah memunculkan elemen dari tumpukan dan tambahkan ke ekspresi postfix. 
Dan jika kita menemukan '(' maka, jangan masukan kedalam kondisi (dibuang).

"""

