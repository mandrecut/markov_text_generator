import sys
import textwrap
from markov import MarkovChar, MarkovWord

if __name__ == '__main__':

    fname = "./datatxt/sherlock_holmes.txt"

    if(sys.version_info[0] < 3):
        # Python 2	
        with open(fname, "r") as f:
            x = f.read().decode("UTF-8")
    else:
        # Python 3
        with open(fname, "r", encoding="utf-8") as f:
            x = f.read()

    mc = MarkovChar(6)

    mc.learn(x)

    print(textwrap.fill(mc.generate(500), width=72))

    mw = MarkovWord(2)

    mw.learn(x)

    print(textwrap.fill(mw.generate(100), width=72))

