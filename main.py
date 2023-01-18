from logic import bet
from decouple import config

money = int(config('MY_MONEY'))

while True:
    if money == 0:
        print("GO OUT")
        break
    play = input("будете играть?")
    if play == 'да':
        slot = int(input('слот для ставки (1-30):'))
        amount = int(input(f'деньги для ставки (1-{money}):'))
        money += bet(slot, amount)
    else:
        print('BYE')
        break


print(money)