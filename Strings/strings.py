# Capitalize
# # warning:this change the capital word in sentence to the lower case
sentence = 'i love Python'
cap_sen = sentence.capitalize() 
print(cap_sen)

# Center
sentence = 'Python is awesome'
print(len(sentence))
new_sentence = sentence.center(25, '*') #second argument is optional(without means default_arg==empty-space)
print(new_sentence)

# Casefold
# Casefold() as an aggressive lower() method
text = 'groß'

# convert text to lowercase using casefold()
print('Using casefold():', text.casefold()) # gross


# convert text to lowercase using lower()
print('Using lower():', text.lower())  # groß


# count

string = "Python is awesome, isn't it?"
substring = "is"

# count after first 'i' and before the last 'i'
count = string.count(substring, 8, 25) # Start and end indexes are optional

print(count)

# endswith

text = "Python programming is easy to learn."
print(len(text))

result = text.endswith('learn.', 7) # 7 is start of searching
print(result)

result = text.endswith('is', 7, 26)   # start and end of searching
print(result)

result = text.endswith('easy', 7, 26)
print(result)

# passing tuple as the suffix in endswith

text = "programming is easy"
result = text.endswith(('programming', 'python'))
print(result)

result = text.endswith(('python', 'easy', 'java'))
print(result)

# With start and end parameter
# 'programming is' string is checked
result = text.endswith(('is', 'an'), 0, 14) # true
print(result)

# expandtabs
# each tab will replaced by default to 8 empty_spaces counting includes chars before\t
str = "xyz\t12345\tabc"
print('Original String:', str)
# default is 8
result = str.expandtabs() # equal to line 65
print(result)
# tabsize is set to 2
print('Tabsize 2:', str.expandtabs(2))

print('Tabsize 3:', str.expandtabs(3))

print('Tabsize 4:', str.expandtabs(4))

print('Tabsize 5:', str.expandtabs(5))

print('Tabsize 6:', str.expandtabs(6))


# encode # cool it is

# unicode string
string = 'pythßän!'

# print string
print('The string is:', string)

# ignore error
print('The encoded version (with ignore) is:', string.encode("ascii", "ignore"))


# replace error
print('The encoded version (with replace) is:', string.encode("ascii", "namereplace"))

print('The encoded version (with replace) is:', string.encode("ascii", "backslashreplace"))
print('The encoded version (with replac')
quote = 'Do small things with great love'

# Substring is searched in 'hings with great love'
print(quote.find('small things', 10))


# Substring is searched in ' small things with great love' 
print(quote.find('small things', 2))

# Substring is searched in 'hings with great lov'
print(quote.find('o small ', 10, -1))


# Substring is searched in 'll things with'
print(quote.find('things ', 6, 20))

