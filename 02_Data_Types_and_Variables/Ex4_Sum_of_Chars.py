n = int(input())
ascii_sum = 0
for i in range(n):
    current_char = input()
    ascii_sum+= ord(current_char)

print(f'The sum equals: {ascii_sum}')