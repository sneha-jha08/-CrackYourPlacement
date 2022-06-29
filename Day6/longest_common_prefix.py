class Solution:
    def longestCommonPrefix(self, s: List[str]) -> str:
        if len(s)==0:
            return ''
        s1=min(s)
        s2=max(s)
        
        for i , ch in enumerate(s1): 
            if ch !=s2[i]:
                return s1[:i]
        return s1
        
        
         ##compare alphabetically smallest=s1 and largest str=s2 character wise , if char not in s2 then return s1[:i], else return s1
