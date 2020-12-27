
'''
    Given a target string and list of words.
    Return True of the target string can be generated from the list
    Else return False
'''
# Using memoization to store result of calculated function: memo[target] = True or False

def canConstruct(target, words, memo={}):

    if target in memo: return memo[target]

    # Base case
    if target == '': return True

    for word in words:
        if word == target[:len(word)]:
            suffix = target[len(word):]
            if canConstruct(suffix, words):
                memo[target] = True
                return memo[target]
    memo[target] = False
    return memo[target]

print(canConstruct('skateboard', ['bo', 'rd', 'ate', 'sk']))    #False
print(canConstruct('skateboard', ['ska', 'teb', 'oar', 'd']))   # False
print(canConstruct('google', ['go', 'oo', 'gle','o']))          # True
print(canConstruct('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaf', ['aaa', 'a', 'aa', 'aaaa','aaaaaa', 'aaaaa']))