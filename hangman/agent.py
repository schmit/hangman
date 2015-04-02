import string
import random

class Agent:
    def __init__(self):
        self.available = [x for x in string.ascii_lowercase]

    def getWord(self, wordlist):
        self.wordlist = wordlist[:]
        return random.sample(wordlist, 1)[0]

    def getGuess(self, hiddenWord):
        ch = random.sample(self.available, 1)[0]
        self.available.remove(ch)
        return ch

class HumanAgent:
    def __init__(self):
        self.available = [x for x in string.ascii_lowercase]

    def getWord(self, wordlist):
        while True:
            word = raw_input('Pick a word: ')
            word = word.lower()
            if word in wordlist:
                return word
            else:
                print 'Word not recognized, please try again'

    def getGuess(self, hiddenWord):
        while True:
            ch = raw_input('Next guess: ')
            if ch in self.available:
                self.available.remove(ch)
                return ch
            else:
                print 'Not a valid guess, please pick from:'
                print ' '.join(self.available)
