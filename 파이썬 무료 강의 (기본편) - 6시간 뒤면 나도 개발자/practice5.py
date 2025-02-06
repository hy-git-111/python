# 계좌에 입금하는 프로그램

# 계좌 생성
def account():
    print("새로운 계좌가 생성되었습니다.")

# 입금
def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
    return balance + money

# 출금
def withdraw(balance, money):
    if balance >= money:
        total = balance - money
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(total))
        return total
    else:
        print("잔액이 부족합니다. 잔액은 : {0} 원입니다.".format(balance))
        return balance

# 야간 출금
def nightWithdraw(balance, money):
    if balance >= money:
        commission = 100
        total = balance - money - commission
        print("수수료는 {0}원입니다. 잔액은 : {1} 원입니다.".format(commission, total))
        return commission, total
    else:
        print("잔액이 부족합니다. 잔액은 : {0} 원입니다.".format(balance))
        return balance
    

balance = 0
balance = deposit(balance, 1000)
print(balance)

balance = withdraw(balance, 5000)
print(balance)

balance = withdraw(balance, 50)
print(balance)

comission, balance = nightWithdraw(balance, 500)