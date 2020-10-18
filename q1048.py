class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        l = {c:0 for c in words}
        s = set(words)
        for c in words:
            if l[c] == 0:
                self.help(c, s, l);
        return max(l.values())


    def help(self,element,element_set,chain_length):
        max_sub_element = 0
        for i in range(len(element)):
            new_element = element[0:i] + element[i+1:]
            if new_element in element_set:
                if chain_length[new_element] == 0:
                    self.help(new_element,element_set, chain_length)
                max_sub_element = max(max_sub_element, chain_length[new_element])
            chain_length[element] = 1 + max_sub_element