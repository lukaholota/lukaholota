from typing import List

def longestCommonPrefix(strs: List[str]) -> str: 
    word1 = list(strs[0])
    word2 = list(strs[1])
    word3 = list(strs[2])
    prefix = ''
    index = 0
    while True:
        if word1[index] == word2[index] and word1[index] == word3[index]:
            prefix = prefix + word1[index]
        else:
            break
        index = index + 1
    return prefix


def checkIfAllNumbersEqual(numbers: List[int]):
    for num in numbers:
        first_number = numbers[0]
        if num != first_number:
            return False
    return True
'''print(checkIfAllNumbersEqual([1,1,1]))'''

strs = ['kucumbra', 'catapulta', 'caban']
print(longestCommonPrefix(strs))