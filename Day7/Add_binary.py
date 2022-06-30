class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2)+int(b,2)).replace("0b", "")
			
			#  bin function changes decimal to binary string
			#  int changes string to decimal given we know what type of number does the string contain, in our case 2 means our string contains a binary number
