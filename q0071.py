class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        s = path.split("/")
        stack = []
        for i in s:
            if i == "" or i == ".":
                continue
            elif i == "..":
                if len(stack) != 0:
                    stack.pop()
            else:
                stack += [i]
        return "/" + '/'.join(stack)
