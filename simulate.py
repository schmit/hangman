from hangman.hangman import Hangman
from hangman.agent import Agent

def parseWordFile(filename):
    wordlist = []
    with open(filename, 'r') as f:
        for line in f:
            wordlist.append(line.strip().lower())

    return wordlist

# options
nsim = 1000
lives = 10
filename = 'wordsEn.txt'

# setup simulation
wins = 0
wordlist = parseWordFile('data/' + filename)

# run games
for sim in xrange(nsim):
    a = Agent()
    h = Hangman(a, a, wordlist, lives=lives, verbose=False)
    outcome = h.play()
    wins += outcome

print 'Performance: {} / {}'.format(wins, nsim)

