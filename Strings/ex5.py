# Assign to a variable in your program a triple-quoted string that contains your
# favorite paragraph of text — perhaps a poem, a speech, instructions to bake a cake, 
# some inspirational verses, etc.

# Write a function which removes all punctuation from the string, breaks the string into a 
# list of words, and counts the number of words in your text that contain the letter “e”.
# Your program should print an analysis of the text like this:

# Your text contains 243 words, of which 109 (44.8%) contain an "e".

import string
three_string = ''' All through eternity
Beauty unveils His exquisite form
in the solitude of nothingness;
He holds a mirror to His Face
and beholds His own beauty.
he is the knower and the known,
the seer and the seen;
No eye but His own
has ever looked upon this Universe.
His every quality finds an expression:
Eternity becomes the verdant field of Time and Space;
Love, the life-giving garden of this world.
Every branch and leaf and fruit
Reveals an aspect of His perfection-
They cypress give hint of His majesty,
The rose gives tidings of His beauty.
Whenever Beauty looks,
Love is also there;
Whenever beauty shows a rosy cheek
Love lights Her fire from that flame.
When beauty dwells in the dark folds of night
Love comes and finds a heart
entangled in tresses.
Beauty and Love are as body and soul.
Beauty is the mine, Love is the diamond.
They have together
since the beginning of time-
Side by side, step by step eee.
'''

def removes_all(strings,content):
    punctuation = string.punctuation
    for n in strings:
        if n in punctuation:
            strings = strings.replace(n,'')

    strings = strings.replace('\n', ' ').strip()
    # strings = strings.replace(' ', '')
    list_of_words = strings.split(' ')
    count_e = strings.count(content)
    len_strings = len(list_of_words)
    percentage_e = (count_e / len_strings)*100
    # Your text contains 243 words, of which 109 (44.8%) contain an "e".
    return f'Your text contains {len_strings} words, of which {count_e} ({round(percentage_e,2)}%) contain an "{content}".'
    

print(removes_all(three_string,'e'))
