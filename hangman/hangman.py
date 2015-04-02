class Hangman:
    '''
    Hangman class implement the game dynamics of Hangman

    To run, it requires a Chooser agent, a Guesser agent, and a list of words
    '''
    def __init__(self, chooser, guesser, wordlist, lives=10, verbose=True, debug=False):
        # the agents
        self.chooser = chooser
        self.guesser = guesser

        self.wordlist = wordlist  # the words available
        self.lives = lives  # number of lives for guesser

        self.verbose = verbose
        self.debug = debug

        self.guesses = ''

    def play(self):
        self.printStart()
        self.getWord()
        self.nguesses = 0
        self.win = False
        while self.lives > 0:
            self.printRound()

            self.getGuess()
            self.nguesses += 1

            if len(self.missing_chars) == 0:
                self.win = True
                break

        self.printOutcome()
        return self.win

    def getWord(self):
        self.word = self.chooser.getWord(self.wordlist)
        self.missing_chars = {ch for ch in self.word}
        if self.debug:
            print 'Hidden word: {}'.format(self.word)

    def hideWord(self):
        output = ''
        for ch in self.word:
            if ch in self.missing_chars:
                output += '. '
            else:
                output += ch + ' '
        return output

    def getGuess(self):
        guess = self.guesser.getGuess(self.hideWord())
        # save guess for possible analysis
        self.guesses += guess
        if self.verbose:
            print 'Guess: {}'.format(guess)
        if guess in self.missing_chars:
            self.missing_chars.remove(guess)
        else:
            self.lives -= 1

    def printRound(self):
        if self.verbose:
            print '-' * 20
            print 'Round: {} \t Lives left: {}'.format(self.nguesses, self.lives)
            print 'Current word: {}'.format(self.hideWord())

    def printStart(self):
        if self.verbose:
            print '='*20
            print 'HANGMAN GAME'
            print 'lives: {}'.format(self.lives)
            print '='*20

    def printOutcome(self):
        if self.verbose:
            print '=' * 20
            if self.win:
                print 'The guesser wins!'
                print 'Lives left: {}'.format(self.lives)
            else:
                print 'The chooser wins!'

            print 'Guesses used: {}'.format(self.nguesses)
            print 'The word the chooser was looking for: {}'.format(self.word)

    def summary(self):
        return {'win': self.win, 'nguesses': self.nguesses, 'nlives': self.lives,
            'word': self.word, 'guesses': self.guesses, 'missing': self.missing_chars}

