class Solution:
    def isValid(self, s: str) -> bool:
        # opened = []

        # for c in s:
        #     if c == ")":
        #         if not opened: return False
        #         if opened and opened.pop() != "(":
        #             return False
        #     elif c == "}":
        #         if not opened: return False
        #         if opened and opened.pop() != "{":
        #             return False
        #     elif c == "]":
        #         if not opened: return False
        #         if opened and opened.pop() != "[":
        #             return False
        #     else:
        #         opened.append(c)
        
        # return not opened

        # d = dict(("()", "[]", "{}"))
        d = {"(":")", "{":"}", "[":"]"}
        opened = []

        for c in s:
            if c in "({[":
                opened.append(c)
            elif not opened or c != d[opened.pop()]:
                return False
        
        return not opened