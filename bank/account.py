class Account():
    bankAccount = {} #계좌번호, 잔고
    name = {} #계좌번호, 이름
    total_deposit = 0 # 은행 잔고
    loan_list = {} # 대출금

    #계좌개설
    def makeAccount (self):        
        print("======계좌개설======")

        flag = 0

        #계좌번호에는 음수x
        try:
            accountNumber = int(input("계좌번호: "))
            if accountNumber < 0:
                raise NotImplementedError
            for i in self.bankAccount:
                if accountNumber == i:
                    print("이미 존재하는 계좌번호입니다.") # 중복 예외처리
                    flag = 1
                    break
            
            if flag == 0:
                accountName = input("이름: ") #이름 정수이면 x
                if accountName.isdigit() == False:
                    self.name[accountNumber]= accountName
                    self.loan_list[accountNumber] = 0
                    try:
                        accountMoney = int(input("예금: ")) # 계좌 음수일 수x
                        if accountMoney < 0:
                            raise NotImplementedError()
                        self.bankAccount[accountNumber]= accountMoney
                        Account.total_deposit = Account.total_deposit + accountMoney * 0.93 #예금의 7%를 제외한 금액 대출 가능
                        print("##계좌개설을 완료하였습니다.##")
                        print("====================")
                    except:
                        print("금액 입력이 올바르지 않습니다.")
                else:
                    print("이름 입력이 올바르지 않습니다.")
        except:
            print("계좌번호 입력이 올바르지 않습니다.")

    #입금하기
    def putMoney(self):
        print("======입금하기======")
        try:
            message1 = int(input("입금하실 계좌번호를 입력해주세요: "))
            if message1 in self.bankAccount.keys():
                print("계좌번호: ", message1, "/ 이름: ", self.name[message1],"/ 잔액: ", self.bankAccount[message1])
                message2 = int(input("입금하실 금액을 입력해주세요: "))
                if message2 >= 0:
                    self.bankAccount[message1] += message2
                    print("계좌번호: ", message1, "/ 이름: ", self.name[message1],"/ 잔액: ", self.bankAccount[message1])
                    Account.total_deposit = Account.total_deposit + message2 * 0.93 #예금의 7%를 제외한 금액 대출 가능
                else:
                    print("금액 입력이 올바르지 않습니다.") # 음수 예외처리
            else:
                print("해당 계좌가 존재하지 않습니다.")
        except: 
            print("===잘못된 계좌번호 입니다.===")

    #출금하기
    def pullMoney(self):
        print("======출금하기======")
        try:
            message1 = int(input("출금하실 계좌번호를 입력해주세요: "))
            if message1 in self.bankAccount.keys():
                print("계좌번호: ", message1, "/ 이름: ", self.name[message1],"/ 잔액: ", self.bankAccount[message1])
                message2 = int(input("출금하실 금액을 입력해주세요: "))
                if self.bankAccount[message1] < message2: #돈 초과해서x
                    print("돈이 부족합니다")
                    print("계좌번호: ", message1, "/ 이름: ", self.name[message1],"/ 잔액: ", self.bankAccount[message1])
                elif message2 < 0: #음수 금액x
                    print("금액 입력이 올바르지 않습니다.")
                else:
                    self.bankAccount[message1] -= message2
                    print("계좌번호: ", message1, "/ 이름: ", self.name[message1],"/ 잔액: ", self.bankAccount[message1])
            else: # dictiomary에 존재하지 않는 계좌번호
                print("해당 계좌가 존재하지 않습니다.")
        except: 
            print("\n===잘못된 계좌번호 입니다.===")

    #전체조회
    def searchAll(self):
        for i in self.bankAccount:
            print("계좌번호: ", i, "/ 이름: ", self.name[i],"/ 잔액: ", self.bankAccount[i])
    
    def endAccount(self):
        print("이용해주셔서 감사합니다!")

    #대출
    def loan(self):
        print("======대출하기======")
        try:
            checkaccount = int(input("대출받을 계좌번호를 입력해주세요: "))
            if checkaccount in self.bankAccount.keys():
                print("계좌이름:", self.name[checkaccount])
                print("계좌잔고:", self.bankAccount[checkaccount], "원")
                print("대출 가능 금액:", Account.total_deposit, "원")
                loan = int(input("대출받을 금액을 입력해주세요: "))
                if loan > Account.total_deposit:
                    print("대출 가능 금액 초과")
                elif loan < 0:
                    print("금액 입력이 올바르지 않습니다.")
                else:
                    self.bankAccount[checkaccount] += loan
                    Account.total_deposit -= loan
                    self.loan_list[checkaccount] += loan
                    print('\n##계좌잔고: ', self.bankAccount[checkaccount], "원 / 대출금: ", self.loan_list[checkaccount], "원##")
                    print("##대출이 완료되었습니다##")
                    print("====================")
            else:
                print("해당 계좌가 존재하지 않습니다.")
        except:
            print("\n===잘못된 계좌번호 입니다.===")

    #대출상환
    def loan_repayment(self):
        print("======대출상환======")
        try:
            checkaccount = int(input("대출상환할 계좌번호를 입력해주세요: "))
            if checkaccount in self.bankAccount.keys():
                print("계좌이름:", self.name[checkaccount])
                print("계좌잔고:", self.bankAccount[checkaccount], "원")
                print("대출금: ", self.loan_list[checkaccount], "원")
                LR = int(input("대출상환할 금액을 입력해주세요: "))
                if LR > self.loan_list[checkaccount]:
                    print("대출금 초과")
                elif LR < 0:
                    print("금액 입력이 올바르지 않습니다.")
                else:
                    self.bankAccount[checkaccount] -= LR
                    self.loan_list[checkaccount] -= LR
                    Account.total_deposit += LR
                    print('\n##계좌잔고: ', self.bankAccount[checkaccount], "원 / 대출금: ", self.loan_list[checkaccount], "원##")
                    print("##대출상환이 완료되었습니다##")
                    print("====================")
            else:
                print("해당 계좌가 존재하지 않습니다.")
        except:
            print("\n===잘못된 계좌번호 입니다.===")