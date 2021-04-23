from account import *

class Bank(Account):

    #메인
    def main(self):
        # try:
            print("\n======Bank Menu=====")
            print("1. 계좌개설\n2. 입금하기\n3. 출금하기\n4. 전체조회\n5. 종료하기")
            print("====================")
            select = int(input())
            return select

        # except:
        #     print("===잘못된 입력입니다.===")

menu = 0
while True:
    person = Bank()
    menu = person.main()
    if menu == 5: # 종료하기
        print("##프로그램을 종료합니다##")
        break
    elif menu == 1: # 계좌개설
        person.make_account()
    elif menu == 2: # 입금하기
        person.deposit()
    elif menu == 3: # 출금하기
        person.withdraw()
    elif menu == 4: # 전체조회
        person.manage()