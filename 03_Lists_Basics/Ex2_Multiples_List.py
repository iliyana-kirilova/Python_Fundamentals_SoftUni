factor = int(input())
count= int(input())

list_of_numbers = [factor * i for i in range(1, count + 1)]

print(list_of_numbers)