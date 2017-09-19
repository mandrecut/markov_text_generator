from collections import defaultdict, Counter
import progressbar
import random
import re

class MarkovChar(object):

    def __init__(self, order=1):
        """
        Input: Markov chain order >= 1.
        Initializes the dictionary of char transitions.
        """
        self.dct = defaultdict(Counter)
        self.order = order

    def learn(self, txt):
        """
        Input: some text.
        Returns the dictionary and the state transition probabilities.
        """
        bar = progressbar.ProgressBar()
        for n in bar(range(len(txt)-self.order)):
            self.dct[txt[n:n+self.order]][txt[n+self.order]] += 1
        for k in self.dct:
            s = float(sum(self.dct[k].values()))
            for v in self.dct[k]:
                self.dct[k][v] = self.dct[k][v]/s

    def nextstate(self, state):
        """
        Input: current Markov state. 
        Returns next Markov state.
        """
        c, s, r = "", 0, random.random()
        for c in self.dct[state]:
            s = s + self.dct[state][c]
            if s >= r: 
                break			
        state = state[1:self.order] + c
        return state

    def generate(self, length):
        """
        Input: length (number of chars) of text to be generated.
        Returns random text starting from an uppercase char, 
        with a minimum lenght, until the last sentence ends in .?!
        """
        keys = list(self.dct.keys())
        state = random.choice(keys)
        while state[0] not in "QWERTYUIOPASDFGHJKLZXCVBNM":
            state = random.choice(keys)
        n, out = 0, [state]
        while n<length or state[self.order-1] not in ".?!":
            n, state = n+1, self.nextstate(state)
            out.append(state[self.order-1])		
        return "".join(out)

class MarkovWord(object):

    def __init__(self, order=1):
        """
        Input: Markov chain order >= 1.
        Initializes the dictionary of word transitions.
        """
        self.dct = defaultdict(Counter)
        self.order = order

    def learn(self, txt):
        """
        Input: some text.
        Returns the dictionary and the state transition probabilities.
        """
        x = re.findall(r"[\w']+|[.,!?;]", txt)
        bar = progressbar.ProgressBar()
        for n in bar(range(len(x)-self.order)):
            k = []
            for i in range(0,self.order):
                k.append(x[n+i])
            k = tuple(k)
            self.dct[k][x[n+self.order]] += 1
        for k in self.dct:
            s = float(sum(self.dct[k].values()))
            for v in self.dct[k]:
                self.dct[k][v] = self.dct[k][v]/s

    def nextstate(self, state):
        """
        Input: current Markov state. 
        Returns next Markov state.
        """
        state, w, s, r = tuple(state),"", 0, random.random()
        for w in self.dct[state]:
            s = s + self.dct[state][w]
            if s >= r: 
                break
        state = list(state)
        state[0:self.order-1] = state[1:self.order]
        state[self.order-1] = w
        return state

    def generate(self, length):
        """
        Input: length (number of words) of text to be generated. 
        Returns random text starting from an uppercase word, with 
        a minimum lenght of words, until the last sentence ends in .?!
        """
        keys = list(self.dct.keys())
        state = random.choice(keys)
        while state[0][0] not in "QWERTYUIOPASDFGHJKLZXCVBNM":
            state = random.choice(keys)
        out = [state[0]]
        for i in range(1,self.order):
            if state[i] not in ".,;:?!-'":
                out.append(" ")
            out.append(state[i])
        n = self.order
        while n<length or state[self.order-1] not in ".?!":
            n, state = n+1, self.nextstate(state)
            if state[self.order-1] not in ".,;:?!-'":
                out.append(" ")
            out.append(state[self.order-1])
        return "".join(out)
