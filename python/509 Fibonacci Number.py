class Solution:
    def __init__(self):
        self.fb = [0] * 31

    def fib(self, n: int) -> int:
        # fb = [0] * 31
        # fb[0] = 0
        # fb[1] = 1
        
        # for i in range(2, n+1):
        #     fb[i] = fb[i-1] + fb[i-2]
        
        # return fb[n]

        # fb = [0] * 31

        # if n <= 1:
        #     return n
        
        # if self.fb[n] == 0:
        #     self.fb[n] = self.fib(n-1) + self.fib(n-2)
        
        # return self.fb[n]

        if n <= 1:
            return n
        
        fib1 = self.fb[n-1] if self.fb[n-1] != 0 else self.fib(n-1)
        fib2 = self.fb[n-2] if self.fb[n-2] != 0 else self.fib(n-2)

        self.fb[n] = fib1 + fib2

        return self.fb[n]