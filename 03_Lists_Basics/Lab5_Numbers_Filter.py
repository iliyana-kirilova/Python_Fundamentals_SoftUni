n = int((input()))

list_numbers = []
for i in range(n):
    current_number = int(input())
    list_numbers.append(current_number)

command = input()
new_list = []
if command == "even":
    new_list = [x for x in list_numbers if x%2==0]
elif command =="odd":
    new_list = [x for x in list_numbers if x%2!=0]
elif command =="negative":
    new_list = [x for x in list_numbers if x<0]
elif command =="positive":
    new_list = [x for x in list_numbers if x>=0]

print(new_list)