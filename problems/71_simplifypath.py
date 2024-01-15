class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        s = ""
        for i in path:
            if i == "/":
                if s == "..":
                    stack.pop()
                    s = ""
                if len(s) > 0:
                    stack.append(s)
                    s = ""
            else:
                s += i

        result = "/" + "/".join(stack)

        return result


solution_instance = Solution()
result = solution_instance.simplifyPath("//users//var//local//..//..//test/")
print(result)
