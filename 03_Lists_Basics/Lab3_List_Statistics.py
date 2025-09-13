n = int((input()))

list_positive_numbers = []
list_negative_numbers = []

for i in range(n):
    current_number = int(input())
    if current_number>0:
        list_positive_numbers.append(current_number)
    else: list_negative_numbers.append(current_number)


sum_negative_numbers = 0

for i in list_negative_numbers:
    sum_negative_numbers+=i

print(list_positive_numbers)
print(list_negative_numbers)
print(f'Count of positives: {len(list_positive_numbers)}')
print(f'Sum of negatives: {sum_negative_numbers}')
