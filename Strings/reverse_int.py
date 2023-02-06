class Solution:
    def reverse(self, x: int) -> int:
        index = 1
        s = list(str(x))
        prefix = None
        i = 0
        j = len(s) - 1
        if s[i] == "-":
            prefix = s[i]
            i += 1
        while i < j:
            s[j], s[i] = s[i], s[j]
            i += 1
            j -= 1
        val = int("".join(s))
        if -2 ** 31 <= val <= 2 ** 31 - 1:
            return val
        else:
            return 0


s = Solution()
print(s.reverse(1534236469))
