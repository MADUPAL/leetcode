class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # stack = []
        # operator = set(["+", "-", "*", "/"])
        # for token in tokens:
        #     if token not in operator:
        #         stack.append(int(token))
        #     else:
        #         y = stack.pop()
        #         x = stack.pop()
        #         if token == "/":
        #             if x / y < 0:
        #                 tmp = int(math.ceil(x/y))
        #             else:
        #                 tmp = x//y
        #             stack.append(tmp)
        #         elif token == "*":
        #             stack.append(x*y)
        #         elif token == "+":
        #             stack.append(x+y)
        #         elif token == "-":
        #             stack.append(x-y)
        # return stack.pop()

        stack = []
        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                y = stack.pop()
                x = stack.pop()
                stack.append(x-y)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                y = stack.pop()
                x = stack.pop()
                stack.append(int(x/y))
            else:
                stack.append(int(token))
        
        return stack.pop()
    
        # stack = []

        # for token in tokens:
        #     if token == "+":
        #         stack.append(stack.pop() + stack.pop())
        #     elif token == "-":
        #         a = stack.pop()
        #         b = stack.pop()
        #         stack.append(b-a)
        #     elif token == "*":
        #         stack.append(stack.pop() * stack.pop())
        #     elif token == "/":
        #         a = stack.pop()
        #         b = stack.pop()
                
        #         stack.append(int(b / a))
        #     else:
        #         stack.append(int(token))
        # print(stack)
        # return stack[0]