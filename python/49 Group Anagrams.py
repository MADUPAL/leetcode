class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hm = {}
        # ans = []

        # for s in strs:
        #     temp = {}
        #     for c in s:
        #         if c not in temp:
        #             temp[c] = 0
        #         temp[c] += 1
        #     hm[s] = temp
        
        # for s in strs:
        #     flag = False
        #     for array in ans:
        #         if hm[array[0]] == hm[s]:
        #             array.append(s)
        #             flag = True
        #             break
            
        #     if not flag:
        #         ans.append([s])
        
        # return ans

        ### O(mnlogn)
        # hm = {}
        # ans = []

        # for s in strs:
        #     sortedStr = ''.join(sorted(s))
        #     if sortedStr not in hm:
        #         hm[sortedStr] = []
        #     hm[sortedStr].append(s)
        
        # for v in hm.values():
        #     ans.append(v.copy())
        
        # return ans

        ## O(mn)
        hm = defaultdict(list)

        for s in strs:
            cnt = [0] * 26
            for c in s:
                cnt[ord(c)-ord('a')] += 1

            hm[tuple(cnt)].append(s)
        
        return hm.values()