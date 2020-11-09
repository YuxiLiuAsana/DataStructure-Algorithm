class Solution:
    def reverseWords(self, s: str) -> str:
        #" ".join(s.split()[::-1])
        return " ".join(list(filter(lambda x: x != "", s.strip().split(" ")))[::-1])