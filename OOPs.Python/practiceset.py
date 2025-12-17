# create account class with 2 attributes - balance & account no.



class Account:
    def _init_ (self,bal, acc):
        self.balance = bal
        self.account_no =acc

        #debit method
        def debit(self, amount):
            self.balance -= amount
        print("Rs.", "amount" , "was debited")
        print("total balance =", self.get_balance())

    def  credit(self, amount):
            self.balance += amount
    print("Rs.", " amount ", "was credited")
    print("total balance =",   self.get_balance())


    def get_balance(self):
      return self.balance

acc1 = Account(10000, 12345)
acc1.debit (10000)                                         # print(acc1.balance)
acc1.credit(500)
acc1.debit (40000)                                         # print(acc1.balance)
acc1.credit(100000)
