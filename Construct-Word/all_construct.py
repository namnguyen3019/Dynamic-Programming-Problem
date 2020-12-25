'''
    Given a target string and a list of words:
    Return all ways to construct the string using words in the list
    Or return empty list if False
'''


def allConstruct(target, words):

    if target == '': return [[]]
    result = []
    for word in words:
        if target.find(word) == 0:
            suffix = target[len(word):]
            # Ways to build suffix
            suffixWays = allConstruct(suffix, words)

            targetWays = list(map(lambda way: [word] + way, suffixWays))

            for elem in targetWays:
                result.insert(0, elem)

    return result

print(allConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
print(allConstruct('skateboard', ['ska', 'teb', 'oar', 'd']))
print(allConstruct('google', ['go', 'oo', 'gle','o']))
print(allConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']))
print(allConstruct('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaf', ['a', 'aa','aaa', 'aaaa', 'aaaaa']))

def bestConstruct(target, words):
    allWays = allConstruct(target, words)
    if allWays is None: return
    min_path = allWays[0]

    for path in allWays:
        if len(path) < len(min_path):
            min_path = path
    
    return min_path

print(bestConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']))