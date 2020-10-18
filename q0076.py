class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        cnt_t = collections.Counter(t)
        cnt_s = {}
        finish = set()
        important_stack = collections.deque()
        min_len = len(s) + 1
        ret = ""
        for i in range(len(s)):
            if s[i] in cnt_t:
                # add i into important stack
                important_stack.append(i)
                # add i into cnt_s
                if not s[i] in cnt_s:
                    cnt_s[s[i]] = 0
                cnt_s[s[i]] += 1
                if cnt_s[s[i]] == cnt_t[s[i]]:
                    finish.add(s[i])
                if len(finish) == len(cnt_t):
                    while cnt_s[s[important_stack[0]]] - 1 >= cnt_t[s[important_stack[0]]]:
                        cnt_s[s[important_stack[0]]] -= 1
                        important_stack.popleft()
                    if i + 1 - important_stack[0] < min_len:
                        min_len = i + 1 - important_stack[0]
                        ret = s[important_stack[0]:i + 1]

        return ret
