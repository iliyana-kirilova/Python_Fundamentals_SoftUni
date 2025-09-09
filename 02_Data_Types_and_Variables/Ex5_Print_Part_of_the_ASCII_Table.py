start_symbol = int(input())
end_symbol = int(input())
current_symbol = []

for i in range(start_symbol, end_symbol+1):
    print(f'{chr(i)}', end=' ')
