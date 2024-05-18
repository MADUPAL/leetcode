from collections import deque
from collections import Counter

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        answer = len(students)
        cnt = Counter(students)

        for sandwich in sandwiches:
            if cnt[sandwich] > 0:
                cnt[sandwich] -= 1
                answer -= 1
            else:
                return answer
        
        return answer