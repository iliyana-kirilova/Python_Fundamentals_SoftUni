forbidden_symbols = [',', '.', '_']

num_of_string = int(input())

for _ in range(num_of_string):
    string = input()
    for symbol in forbidden_symbols:
        if symbol in string:
            print(f'{string} is not pure!')
            break
    else:
        print(f'{string} is pure.')