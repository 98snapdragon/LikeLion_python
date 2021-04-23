class Account():
    account_list = {} #가지고 있는 계좌와 금액 리스트
    name_list = {}
    def make_account(self):
            
        #계좌번호 정수만 입력
        print("\n======계좌개설======\n")
        try:
            account_num = int(input("계좌번호: ")) #계좌는 str->int로 모두 수정
            if account_num < 0:
                raise NotImplementedError #계좌번호, 입금, 출금에서 전부 음수 입력X
            name = input("이름: ")
            if name.isdigit() == False: #이름에 숫자X
                self.name_list[account_num] = name
                try:
                    first_deposit = int(input("예금: "))
                    if first_deposit < 0:
                        raise NotImplementedError
                    self.account_list[account_num] = first_deposit
                    print("##계좌개설을 완료하였습니다##")
                    print("====================")
                except:
                    print("금액 입력이 올바르지 않습니다.")
            else:
                print("이름 입력이 올바르지 않습니다.")
        except:
            print("계좌번호 입력이 올바르지 않습니다.")
               
    def manage(self): #잔액 조회
        print("======전체조회======")
        for i in self.account_list :
            print("계좌번호:", i, "/ 이름:", self.name_list[i], "/ 잔액:", self.account_list[i], "원")
        print("====================")
            
    def deposit(self):
        #계좌를 입력받고
        #해당 계좌에 돈을 입금 해당 계좌 : +=금액
        print("======입금하기======")
        checkaccount = int(input("입금하실 계좌번호를 입력해주세요: "))
        if checkaccount in self.account_list.keys():
            print("계좌이름:", self.name_list[checkaccount])
            print("계좌잔고:", self.account_list[checkaccount], "원")
            balance = int(input("입금하실 금액을 입력해주세요: "))
            #money = self.account_list[checkaccount]+balance
            if balance >= 0:
                self.account_list[checkaccount] += balance
                print('\n##계좌잔고: ', self.account_list[checkaccount], "원##")
                print("##입금이 완료되었습니다##")
                print("====================")
            else:
                print("금액 입력이 올바르지 않습니다.") #음수 입력X
        else:
            print(self.account_list)
            print("해당 계좌가 존재하지 않습니다.")

    def withdraw(self):
        #계좌를 입력받고
        #해당 계좌에서 출금할 금액 입력 -= 금액
        #만약 출금 금액이 잔액보다 크면 불가
        print("======출금하기======")
        try:
            checkaccount = int(input("출금하실 계좌번호를 입력해주세요: "))
            if checkaccount in self.account_list.keys():
                print("계좌이름:", self.name_list[checkaccount])
                print("계좌잔고:", self.account_list[checkaccount], "원")
                withdraw = int(input("출금하실 금액을 입력해주세요: "))
                if withdraw > self.account_list[checkaccount]: #출금 초과
                    print("잔액 부족")
                elif withdraw < 0:
                    print("금액 입력이 올바르지 않습니다.") #음수 입력X
                else:
                    self.account_list[checkaccount] -= withdraw
                    print('\n##계좌잔고: ', self.account_list[checkaccount], "원##")
                    print("##출금이 완료되었습니다##")
                    print("====================")
            else:
                print("해당 계좌가 존재하지 않습니다.")
        except:
            print("\n===잘못된 계좌번호 입니다.===")