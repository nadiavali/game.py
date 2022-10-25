fruit = "banana"
# count = 0
# for char in fruit:
#     if char == "a":
#         count += 1
# print(count)

def count_letter(fruit, char):
    fruit = "banana"
    count = 0
    for i in fruit:
        if i == char:
            count += 1
    return count

print(count_letter(fruit,'a'))
            