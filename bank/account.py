class Account():
    bankAccount = {} #계좌번호, 잔고
    name = {} #계좌번호, 이름

    #계좌개설
    def makeAccount (self):
        print("======계좌개설======")
        accountNumber = int(input("계좌번호: "))
        accountName = input("이름: ")
        accountMoney = int(input("예금: "))
        self.bankAccount[accountNumber]= accountMoney
        self.name[accountNumber]= accountName
        print("##계좌개설을 완료하였습니다.##")

    #입금하기
    def putMoney(self):
        print("======입금하기======")
        message1 = int(input("입금하실 계좌번호를 입력해주세요: "))
        print("계좌번호: ", message1, "/ 이름: ", self.name[message1],"/ 잔액: ", self.bankAccount[message1])
        message2 = int(input("입금하실 금액을 입력해주세요: "))
        self.bankAccount[message1] += message2
        print("계좌번호: ", message1, "/ 이름: ", self.name[message1],"/ 잔액: ", self.bankAccount[message1])

    #출금하기
    def pullMoney(self):
        print("======출금하기======")
        message1 = int(input("출금하실 계좌번호를 입력해주세요: "))
        print("계좌번호: ", message1, "/ 이름: ", self.name[message1],"/ 잔액: ", self.bankAccount[message1])
        message2 = int(input("출금하실 금액을 입력해주세요: "))
        if self.bankAccount[message1] < message2:
            print("돈이 부족합니다")
        else:
            self.bankAccount[message1] -= message2
            print("계좌번호: ", message1, "/ 이름: ", self.name[message1],"/ 잔액: ", self.bankAccount[message1])

    #전체조회
    def searchAll(self):
        for i in self.bankAccount:
            print("계좌번호: ", i, "/ 이름: ", self.name[i],"/ 잔액: ", self.bankAccount[i])
    










    