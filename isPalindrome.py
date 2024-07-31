class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        Num=x
        revNum=0
        if x > -1:
            while x > 0:
                n = x % 10
                x = x // 10
                revNum = revNum*10+n
            if revNum == Num:
                return True
        else:
            return False
