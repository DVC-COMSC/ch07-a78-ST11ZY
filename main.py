
words = input('Enter the list: ').split()

are = ['a', 'r', 'e']
idxlst = []
for i in range (len(words)):
    if are[1] in words[i] and are[0] in words[i] and are[2] in words[i]:
        idxlst.append(words[i]);
print(idxlst)
# ******************************
# Make your Code
# ******************************

# print the words that has 'a', 'r', 'e' in sequence

