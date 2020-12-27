'''
    Given a target string and a list of words:
    Return all ways to construct the string using words in the list
    Or return empty list if False
'''


def allConstruct(target, words):

    table = [[] for i in range(len(target)+1)]

    # There is 1 way to construc empty list: 
    # Assign table[0] to empty list

    table[0] = [[]]

    for i in range(len(target)):
        for word in words:
            if target[i:].find(word) == 0:
                if i + len(word) <= len(target):
                    for way in table[i]:
                        newCombination = way + [word]
                        table[i+len(word)].append(newCombination)
    
    return table[len(target)]
                
    

print(allConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
print(allConstruct('skateboard', ['ska', 'teb', 'oar', 'd']))
print(allConstruct('google', ['go', 'oo', 'gle','o']))
print(allConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']))
print(allConstruct('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaf', ['a', 'aa','aaa', 'aaaa', 'aaaaa']))

# def bestConstruct(target, words):
#     allWays = allConstruct(target, words)
#     if allWays is None: return
#     min_path = allWays[0]

#     for path in allWays:
#         if len(path) < len(min_path):
#             min_path = path
    
#     return min_path

# print(bestConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']))