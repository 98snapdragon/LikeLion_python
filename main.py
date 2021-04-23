from bank import Account

#메인
class Bank(Account):
    def main(self):
        print("\n======Bank Menu=====")
        print("1. 계좌개설\n2. 입금하기\n3. 출금하기\n4. 전체조회\n5. 종료하기")
        print("====================")
        select =int(input())
        return select

menu = 0
while True:
    person = Bank()
    menu = person.main()
    if menu == 1:
        person.makeAccount()
    elif menu == 2:
        person.putMoney()
    elif menu == 3:
        person.pullMoney()
    elif menu == 4:
        person.searchAll()
    elif menu == 5:
        break
    else:
        print("잘못 입력하셨습니다.")






