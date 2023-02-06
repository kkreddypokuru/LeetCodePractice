from typing import List


def reverseString(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    i = 0
    j = len(s) - 1
    while i < j:
        s[j], s[i] =   s[i], s[j]
        i += 1
        j -= 1
    print(s)

s = ['a', 'b', 'c']
reverseString(s)
