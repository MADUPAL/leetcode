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
    
        # pSet = { ")": "(", "]": "[", "}": "{" }
        # stack = []
        # for p in s:
        #     if p not in ")]}":
        #         stack.append(p)
        #     else:
        #         if stack:
        #             t = stack.pop()
        #             if t != pSet[p]:
        #                 return False
        #         else:
        #             return False
        
        # return False if stack else True