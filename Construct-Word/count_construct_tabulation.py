'''
    Given a target string and list of words.
    Return number of way that the target string can be generated from the list
    
'''

def countConstruct(target, words):

    table = [0 for i in range(len(target)+1)]

    # There is 1 way to construct empty string:
    table[0] = 1

    for i in range(len(target)):
        for word in words:
            if target[i:].find(word) == 0:
                if i + len(word) <= len(target):
                    table[i+len(word)] += table[i]
    
    return table[len(target)]


print(countConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
print(countConstruct('skateboard', ['ska', 'teb', 'oar', 'd']))
print(countConstruct('google', ['go', 'oo', 'gle','o']))
print(countConstruct('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaf', ['aaa', 'a', 'aa', 'aaaa','aaaaaa', 'aaaaa']))