'''
    Given a target string and list of words.
    Return number of way that the target string can be generated from the list
    
'''

def countConstruct(target, words):

    if target == '': return 1
    totalCount = 0
    for word in words:
        if target.find(word) == 0:
            suffix = target[len(word):]
            numberOfWays = countConstruct(suffix, words)
            totalCount = totalCount + numberOfWays
    
    return totalCount

print(countConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
print(countConstruct('skateboard', ['ska', 'teb', 'oar', 'd']))
print(countConstruct('google', ['go', 'oo', 'gle','o']))
print(countConstruct('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaf', ['aaa', 'a', 'aa', 'aaaa','aaaaaa', 'aaaaa']))