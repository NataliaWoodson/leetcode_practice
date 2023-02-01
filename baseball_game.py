def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        stack = []
        for operation in operations:
            if operation == "+":
                new_score = stack[-1] + stack[-2]
                stack.append(new_score)
            elif operation == "D":
                new_score = stack[-1] * 2
                stack.append(new_score)
            elif operation == "C":
                stack.pop()
            else:
                stack.append(int(operation))

        return sum(stack)