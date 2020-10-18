class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        split = s.split()
        if len(split) == 0 : return 0
        else: return len(s.split()[-1])