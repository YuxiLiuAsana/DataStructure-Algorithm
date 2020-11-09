class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(list(filter(lambda x: x != "", s.strip().split(" ")))[::-1])