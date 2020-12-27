
'''
    Given a target string and list of words.
    Return True of the target string can be generated from the list
    Else return False
'''

def canConstruct(targetWord, words):

    table = [False for i in range(len(targetWord)+1)]
    
    # Able to generate empty string
    table[0] = True

    for i in range(len(targetWord)):
        for word in words:
            if targetWord[i:].find(word) == 0:
                if table[i] is True and i + len(word) <= len(targetWord):
                    table[i+len(word)] = True
    
    return table[len(targetWord)]

print(canConstruct('skateboard', ['bo', 'rd', 'ate', 'sk']))
print(canConstruct('skateboard', ['ska', 'teb', 'oar', 'd']))
print(canConstruct('google', ['go', 'oo', 'gle','o']))
print(canConstruct('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaf', ['aaa', 'a', 'aa', 'aaaa','aaaaaa', 'aaaaa']))