reversed_list = []
string_of_numbers = input()
original_list = string_of_numbers.split()
for n in original_list:
    reversed_list.append(-int(n))

print(reversed_list)

# numbers_as_list = [int(num) for num in input().split()]
# final_list = [-num for num in numbers_as_list]
# print(final_list)

