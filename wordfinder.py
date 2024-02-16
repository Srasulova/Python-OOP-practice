"""Word Finder: finds random words from a dictionary."""
import random


class WordFinder:
    def __init__(self, path):
        self.file = open(path)
        self.word_lst = self.file.read().split()
        self.file.close()
        print(f"{len(self.word_lst)} words read")

    def random(self):
        return random.choice(self.word_lst)

wf = WordFinder("words.txt")
print(wf.random())