#Implement strStr(). Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
#Return 0 when needle is empty

#Time-complexity: O((n-m+1) * m)

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        if n == 0:
            return 0
        shift = 0
        for i in range(len(haystack) - n + 1):
            if haystack[i:n+shift] == needle:
                return i
            shift += 1
        return -1
