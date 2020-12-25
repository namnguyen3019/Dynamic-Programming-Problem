
'''
    Given a target string and list of words.
    Return True of the target string can be generated from the list
    Else return False
'''

def canConstruct(target, words):

    # Base case
    if target == '': return True

    for word in words:
        if word == target[:len(word)]:
            suffix = target[len(word):]
            if canConstruct(suffix, words):
                return True
    
    return False

print(canConstruct('skateboard', ['bo', 'rd', 'ate', 'sk']))
print(canConstruct('skateboard', ['ska', 'teb', 'oar', 'd']))
print(canConstruct('google', ['go', 'oo', 'gle','o']))
print(canConstruct('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaf', ['aaa', 'a', 'aa', 'aaaa','aaaaaa', 'aaaaa']))