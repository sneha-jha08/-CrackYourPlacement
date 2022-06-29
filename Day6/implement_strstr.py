class Solution:
    def strStr(self, h: str, n: str) -> int:
        for i in range(len(h)-len(n)+1):
            if h[i:i+len(n)]==n:# compare range of string with needle
                return i
        return -1
