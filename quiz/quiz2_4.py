'''
4.
다중상속을 이용하여 카드사의 클래스를 만들고
영화카드는 20% 할인
마트카드는 10% 할인
교통은 10%할인을 받는 카드 class를 구현하시오


테스트코드
<입력>
multi_card=Multi_card()
multi_card.charge(20000)
multi_card.consume(5000,'마트')
multi_card.consume(10000,'영화관')
multi_card.consume(2000,'교통')
multi_card.print()

<출력>
카드가 발급 되었습니다.
20000이 충전되었습니다.
마트에서 4500.0원을 사용했습니다.
영화관에서 8000.0원을 사용했습니다.
교통에서 1800.0원을 사용했습니다.
잔액이 5700.0원 입니다
'''


class Multi_card():
    def __init__(self):
        self.balance = int(0)
        print('카드가 발급 되었습니다.')

    def charge(self, money):
        self.balance += money
        print('{}원이 충전되었습니다.'.format(self.balance))

    def consume(self, money, store):
        if store == '영화관':
            money *= 0.8
            if self.balance < money:
                print('원 잔액이 부족합니다.')
            else:
                self.balance -= money
                print('{}에서 {}원 사용했습니다.'.format(store, money))
        elif store == '마트':
            money *= 0.9
            if self.balance < money:
                print('원 잔액이 부족합니다.')
            else:
                self.balance -= money
                print('{}에서 {}원 사용했습니다.'.format(store, money))
        elif store == '교통':
            money *= 0.9
            if self.balance < money:
                print('원 잔액이 부족합니다.')
            else:
                self.balance -= money
                print('{}에서 {}원 사용했습니다.'.format(store, money))
        else:
            if self.balance < money:
                print('잔액이 부족합니다.')
            else:
                self.balance -= money
                print('{}에서 {}원 사용했습니다.'.format(store, money))

    def print(self):
        print('잔액이 {}원 입니다.'.format(self.balance))
