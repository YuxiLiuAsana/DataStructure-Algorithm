class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        word_dict = {}
        for i, w in enumerate(order):
            word_dict[w] = chr(i+97)
        new_words = []
        new_words_sort = []
        for w in words:
            word = ""
            for i in w:
                print
                word += word_dict[i]
            new_words += [word]
            new_words_sort += [word]
        new_words_sort.sort()
        return new_words_sort == new_words