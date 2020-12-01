class Solution:
    def __init__(self):
        self.number_english_map = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven",
                                   8: "Eight", 9: "Nine", 10: "Ten", \
                                   11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen",
                                   16: "Sixteen", 17: "Seventeen", \
                                   18: "Eighteen", 19: "Nineteen", 20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty",
                                   60: "Sixty", \
                                   70: "Seventy", 80: "Eighty", 90: "Ninety", 0: "Zero"}
        self.ret = []

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        else:
            self.helper(num)
            return " ".join(self.ret)

    def helper(self, num: int) -> None:
        if num == 0:
            return
        elif num < 1000:
            self.numberToWordsLessThanThousand(num)
        elif num < 1e6:
            self.numberToWordsLessThanThousand(num // 1000)
            self.ret += ['Thousand']
            self.numberToWords(num % 1000)
        elif num < 1e9:
            self.numberToWordsLessThanThousand(num // 1e6)
            self.ret += ["Million"]
            self.numberToWords(num % 1e6)
        else:
            self.numberToWordsLessThanThousand(num // 1e9)
            self.ret += ["Billion"]
            self.numberToWords(num % 1e9)

    def numberToWordsLessThanThousand(self, num: int) -> None:
        if num >= 100:
            self.ret += [self.number_english_map[num // 100]]
            self.ret += ['Hundred']
        self.numberToWordsLessThanHundred(num % 100)

    def numberToWordsLessThanHundred(self, num: int) -> None:
        if num != 0:
            if num <= 20:
                self.ret += [self.number_english_map[num]]
            else:
                self.ret += [self.number_english_map[num // 10 * 10]]
                if num % 10 != 0:
                    self.ret += [self.number_english_map[num % 10]]
