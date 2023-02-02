def isValid(s):
        """
        :type s: str
        :rtype: bool
        """

        # Time complexity: O(n)
        # Space complexity: O(n)

        hash_map = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        stack = [ ]

        for char in s:
            if char in hash_map:
                if stack and stack[-1] == hash_map[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return not stack   
