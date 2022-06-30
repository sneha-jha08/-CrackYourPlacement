class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        for i in range(n//2):
            if s[i] != s[-i-1]:
                a = s[:i]+s[i+1:]
                b = s[:n-i-1]+s[n-i:]
                return a == a[::-1] or b == b[::-1]
        return True
