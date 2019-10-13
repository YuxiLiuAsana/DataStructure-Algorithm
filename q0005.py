class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_string = ""
        for i in range(len(s)):
            start, end = i,i
            while start >= 0 and end < len(s) and s[start] == s[end]:
                start -=1
                end += 1
                
            if end-start-1 > len(longest_string):
                longest_string = s[start+1:end]
            
            if i > 0 and s[i-1] == s[i]:
                start, end = (i-1,i)
                while start >=0 and end < len(s) and s[start] == s[end]:
                    start -=1
                    end += 1
                if end-start-1 > len(longest_string):
                    longest_string = s[start+1:end]
        return longest_string
