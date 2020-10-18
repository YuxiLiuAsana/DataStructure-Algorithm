class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        temp1 = []
        count = 0
        ret = []
        for w in words:
            temp = 0
            if count != 0: temp = 1

            if count + len(w) + temp <= maxWidth:
                temp1 += [w]
                count = count + len(w) + temp
            else:
                ret += [self.makeString(temp1, maxWidth)]
                temp1 = [w]
                count = len(w)
        last_str = " ".join(temp1)
        last_str = last_str + (maxWidth - len(last_str)) * " "
        ret += [last_str]
        return ret

    def makeString(self, words, maxWidth):
        if len(words) == 1:
            return words[0] + (maxWidth - len(words[0])) * " "
        else:
            total_len = sum(map(len, words))
            intervals = len(words) - 1
            interval_len = maxWidth - total_len
            small_interval = interval_len // intervals
            big_interval_num = interval_len % intervals
            start = words[0]
            for i in range(1, len(words)):
                plus = ""
                if i <= big_interval_num:
                    plus = " "
                start += (plus + small_interval * " " + words[i])

            return start