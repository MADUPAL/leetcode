class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([c.lower() for c in s if c.isalpha() or c.isnumeric()])
        print(s)
        L, R = 0, len(s)-1

        while L < R:
            if s[L] != s[R]:
                return False
            L += 1
            R -= 1
        return True

        # def check(c):
        #     if (ord('a') <= ord(c) <= ord('z') or
        #         ord('A') <= ord(c) <= ord('Z') or
        #         ord('0') <= ord(c) <= ord('9')):
        #         return True

        #     return False

        # L, R = 0, len(s)-1

        # while L < R:
        #     while L < R and not check(s[L]):
        #         L += 1
        #     while L < R and not check(s[R]):
        #         R -= 1
        #     if s[L].lower() != s[R].lower():
        #         return False
        #     L += 1
        #     R -= 1
        
        # return True