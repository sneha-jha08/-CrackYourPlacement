class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub("[^a-z0-9]",'',s.lower())
        #re.sub is used for substitutions in regular expressions
        return s == ''.join(reversed(s))
      
      
###########################################################################################################################################################################

## Method2 ::
class Solution(object):
    def isPalindrome(self, s):
        k = ''
          for i in s:
              if i.isalpha() or i.isdigit():
                  k += i.lower()
          return k == k[::-1]
      
      
            
###########################################################################################################################################################################

## Method3 ::

class Solution(object):
    def isPalindrome(self, s):
        s = [i for i in s.lower() if i.isalnum()]
    	return s == s[::-1]
