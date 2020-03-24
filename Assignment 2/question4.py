# Anagram Checker
def isAnagram(s1, s2):
    if sorted(s1) == sorted(s2):
        print(s1, 'and', s2, 'is an anagram.')
    else:
        print(s1, 'and', s2, 'is not an anagram.')

print('This program checks if two words are anagrams')
print()
s1 = input('Input word 1: ')
s2 = input('Input word 2: ')
isAnagram(s1, s2)
