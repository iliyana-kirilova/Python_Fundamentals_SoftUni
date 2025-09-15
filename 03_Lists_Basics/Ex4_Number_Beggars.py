numbers = [int(num) for num in input().split(', ')]
beggars = int(input())

current_money = 0
money_beggars = []

for beggar in range(1, beggars + 1):
    for index in range(-1 + beggar, len(numbers), beggars):
        current_money += numbers[index]
    money_beggars.append(current_money)
    current_money = 0

print(money_beggars)