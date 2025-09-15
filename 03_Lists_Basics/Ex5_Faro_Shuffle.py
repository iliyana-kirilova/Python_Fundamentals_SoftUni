string_of_card = input().split()
number_of_shuffles = int(input())

current_string_cards = string_of_card
half_deck = int(len(string_of_card)/2)

for shuffle in range(number_of_shuffles):
    left_side = current_string_cards[:half_deck]
    right_side = current_string_cards[half_deck:]
    current_string_cards = []
    for index in range(len(left_side)):
        current_string_cards.append(left_side[index])
        current_string_cards.append(right_side[index])

print(current_string_cards)
