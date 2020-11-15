import re
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter = []
        digit = []
        for l in logs:
            t = l.split(" ")
            if re.match("[a-z]+", t[1]):
                single_log = " ".join(t[1:] + [t[0]])
                letter += [single_log]
            else:
                digit += [l]
        letter = [x.split(" ")[-1] + " " + " ".join(x.split(" ")[:-1]) for x in sorted(letter)]
        return letter + digit