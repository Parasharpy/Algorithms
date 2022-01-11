#Implement strStr(). Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
#Return 0 when needle is empty


#The average and best-case running time of the Rabin-Karp algorithm is O(n+m), but its worst-case time is O((n-m+1)*m) becasue there can be m comparisons
#worst-case example: haystack = "AAAAA", needle = "AAA"
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        q = 101
        d = 26 #base
        n = len(haystack)
        m = len(needle)
        if m == 0:
            return 0
        if n < m:
            return -1
        p = t = 0
        h = (d**(m-1)) % q
        
        for i in range(m):
            p = (p*d + ord(needle[i])) % q
            t = (t*d + ord(haystack[i])) % q
            
        for i in range(n-m+1):
            if p == t:
                count = 0
                for j in range(m):
                    if haystack[i+j] != needle[j]:
                        count += 1
                        break
                if j == m-1 and count == 0:
                    return i
            if i < n-m:
                t = ((d *(t - ord(haystack[i])*h)) + ord(haystack[i+m])) % q
                if t < 0:
                    t += q
        return -1
