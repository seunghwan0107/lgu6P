class BankAccount:
    def __init__(self,owner,passwd,balance=0):
        self.owner = owner
        self.balance = balance
        self.passwd = passwd

        print(f"{owner}님의 계좌가 잔액 {balance}원으로 개설되었습니다.")
    
    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount}원이 입금되었습니다.")
        else:
            print("0보다 큰 금액을 입금해주세요")
    
    def withdraw(self,amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{amount}원이 출금도되었습니다.")
        else:
            print("출금 금액이 잔액을 초과하거나 잘못되었습니다.")
    
    def get_balance(self):
        pw = input("비번을 입력하세요: ")
        if self.passwd == pw:
            print(f"계좌의 현재 잔액은 {self.balance}")
        else:
            print("비번오류")
    
    def remittance(self,amount,account):  
        #amount 만큼 금액 차감
        self.withdraw(amount)
        #ammount 만큼 account에 입금
        account.deposit(amount)

    def get_balance(self):
        print(f"계좌의 현재 잔액:{self.balance}원입니다.")

#계좌생성

account1 = BankAccount("홍길동",10000)
account1.deposit(1000000)
account1.withdraw(20000)
account1.get_balance()

account2 = BankAccount("고길동",100000)
account2.get_balance()
account2.remittance(2000,account1)
account1.get_balance()
account2.get_balance()