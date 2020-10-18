class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == s2: return True
        c1 = Counter(s1)
        c2 = Counter(s2)
        if not c1 == c2:
             return False

        m1 = {}
        m2 = {}
        # does not exchange on this node
        for i in range(len(s1)-1):
            if s1[i] not in m1:
                m1[s1[i]] = 0
            if s2[i] not in m2:
                m2[s2[i]] = 0
            m1[s1[i]] += 1
            m2[s2[i]] += 1
            if m1 == m2:
                temp = self.isScramble(s1[:i+1],s2[:i+1]) and self.isScramble(s1[i+1:], s2[i+1:])
                if temp: return True
        m1 = {}
        m2 = {}
        # does exchange on this node
        for i in range(len(s1)-1):
            if s1[i] not in m1:
                m1[s1[i]] = 0
            if s2[len(s2)-i-1] not in m2:
                m2[s2[len(s2)-i-1]] = 0
            m1[s1[i]] += 1
            m2[s2[len(s2)-i-1]] += 1
            if m1 == m2:
                temp = self.isScramble(s1[:i+1],s2[len(s2)-1-i:]) and self.isScramble(s1[i+1:], s2[:len(s2)-1-i])
                if temp: return True
        return False
