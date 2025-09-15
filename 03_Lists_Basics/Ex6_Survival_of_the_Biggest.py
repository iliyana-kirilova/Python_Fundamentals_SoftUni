list_of_integers = [int(num) for num in input().split()]
n = int(input())

for removed in range(n):
    list_of_integers.pop(list_of_integers.index(min(list_of_integers)))

print(*list_of_integers, sep=', ')
