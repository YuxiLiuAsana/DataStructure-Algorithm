class Solution(object):
    def queryString(self, S, N):
        """
        :type S: str
        :type N: int
        :rtype: bool
        """
        include = set()
        span = int(math.ceil(math.log(N,2)))
        for i in range(1, span+1):
            for j in range(len(S)):
                if i + j <= len(S):
                    sub_str = S[j:i+j]
                    include.add(int(sub_str,2))
        for k in range(1, N + 1):
            if not k in include:
                return False

        return True