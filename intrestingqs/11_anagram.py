from collections import Counter

string1, string2, string3 = 'acbde', 'abced', 'abcda'
# print(Counter(string1), Counter(string2), Counter(string3))
cnt1, cnt2, cnt3 = Counter(string1), Counter(string2), Counter(string3)

if cnt1 == cnt2:
    print('1 and 2 are anagrams')
if cnt1 == cnt3:
    print('1 and 3 are anagrams')


def anagrams(first, second):
    return Counter(first) == Counter(second)


print(anagrams(string1, string2))
