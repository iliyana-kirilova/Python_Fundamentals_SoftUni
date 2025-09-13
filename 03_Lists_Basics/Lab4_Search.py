n = int((input()))
word = input()

list_texts = []
for i in range(n):
    text = input()
    list_texts.append(text)

new_list = [x for x in list_texts if word in x]

print(list_texts)
print(new_list)
