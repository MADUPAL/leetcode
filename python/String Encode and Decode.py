class Solution:

    def encode(self, strs: List[str]) -> str:
        rslt = ''
        for s in strs:
            rslt += str(len(s))+'/'+s
        
        return rslt

    def decode(self, s: str) -> List[str]:
        # ans = []
        # i, j = 0, 0
        # numStr = ''
        # num = 0
        # while i < len(s) and j < len(s):
        #     if s[i].isnumeric():
        #         numStr += s[i]
        #     elif s[i] == '/':
        #         num = int(numStr)
        #         j = i+1
        #         ans.append(s[j:j+num])
        #         i = j+num-1
        #         numStr = ''
        #         num = 0
        #     i += 1
        ans = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '/':
                j += 1
            length = int(s[i:j])
            ans.append(s[j+1:j+1+length])
            i = j+1+length

        return ans
    
    # class Solution:

    # def encode(self, strs: List[str]) -> str:
    #     rslt = ""
    #     for s in strs:
    #         rslt += str(len(s))+"#"+s
        
    #     return rslt

    # def decode(self, s: str) -> List[str]:
    #     # print(s)
    #     i, j = 0, 0
    #     output = []

    #     while j < len(s):
    #         while s[i] != "#":
    #             i += 1
    #         print(i, j)
    #         num = int(''.join(s[j:i]))
    #         j = i+num+1
            
    #         output.append(s[i+1:j])
    #         i = j
    #     return output