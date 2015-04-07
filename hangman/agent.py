import string
import random


class Agent:
    '''
    Agent picks a random word from the wordlist as chooser.
    Agent picks a random remaining character as guess.

    This simple agent shows the setup of the methods of an Agent.
    '''

    def __init__(self):
        self.available = [x for x in string.ascii_lowercase]

    def getWord(self, wordlist):
        '''
        Returns a word from the wordlist as word to be guessed.

        In this case, we pick a random word from the wordlist
        '''
        self.wordlist = wordlist[:]
        return random.sample(wordlist, 1)[0]

    def getGuess(self, hiddenWord):
        '''
        Returns a character as guess

        In this case, picks randomly from the remaining characters
        '''
        ch = random.sample(self.available, 1)[0]
        self.available.remove(ch)
        return ch


class HumanAgent(Agent):
    '''
    HumanAgent asks user for input using the command line interface
    '''

    def getWord(self, wordlist):
        '''
        Query the user for a word, making sure it is in the word list
        '''
        while True:
            word = raw_input('Pick a word: ')
            word = word.lower()
            if word in wordlist:
                return word
            else:
                print 'Word not recognized, please try again'

    def getGuess(self, hiddenWord):
        '''
        Query the user for a character as guess
        '''
        while True:
            ch = raw_input('Next guess: ')
            if ch in self.available:
                self.available.remove(ch)
                return ch
            else:
                print 'Not a valid guess, please pick from:'
                print ' '.join(self.available)
