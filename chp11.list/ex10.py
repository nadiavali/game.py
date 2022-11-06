# def replace(s, old, new):
#     new = s.replace(old, new)
#     return new

# s = "I love spom! Spom is my favorite food. Spom, spom, yum!"
# print(replace("Mississippi", "i", "I"))
# print(replace(s, "om", "am"))


def replace(s, old, new):
    new1 = s.split()
    print(new1)
    for i in new1:
        if old in i:
            print(i)
            i.replace(old, new)
                return ''.join(new1)

s = "I love spom! Spom is my favorite food. Spom, spom, yum!"
#print(replace("Mississippi", "i", "I"))
print(replace(s, "om", "am"))
