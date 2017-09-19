# Markov text generator

Main usage: building Markov models from text files, and generating random text. 

Two Markov chain Python classes:

- `MarkovChar(order)`: char level 

- `MarkovWord(order)`: word level 

## Basic usage

```python
from markov import MarkovWord

mw = MarkovWord(1)
mw.learn("Some long string, for example an article, or a book.")
print(mw.generate(7))
```
```
Some long article, or a book.
```

The `order` parameter corresponds to the Markov chain order `(>=1)`. 

A large `order` reproduces more from the original text. 

A small `order` generates more random text. 

Methods:

- `learn(txt)`, creates a model given a string `txt`.

- `generate(length)`, generates random text (starting with uppercase) with a minimum `lenght`, until the last sentence ends in `".?!"`


## Char level Markov chain

```python
from markov import MarkovChar
import textwrap

fname = "./datatxt/sherlock_holmes.txt"
with open(fname, "r", encoding="utf-8") as f:
	x = f.read()
mc = MarkovChar(6)
mc.learn(x)
print(textwrap.fill(mc.generate(500), width=72))
```
```
100% |#################################################################|
I crouched his heels, and you thinker and chronicle of San France. All
the whole propriate description, with a pale, haggard. Sherlock Holmes
calmly; 'I would be very kind as my trifling away with the cardboard of
the morning them Miss Stoner, that lay silence, you'll see."  "Oh,
Anstruther woman in than succeeded in communicative was eagerly in the
snow, and eerie in the 22nd instant I saw it all our watching
fuller's-earth,' said Holmes, the matter, and told you against him to
say his eyes. For the next room.
```

## Word level Markov chain

```python
from markov import MarkovWord
import textwrap

fname = "./datatxt/sherlock_holmes.txt"
with open(fname, "r", encoding="utf-8") as f:
	x = f.read()
mw = MarkovWord(2)
mw.learn(x)
print(textwrap.fill(mw.generate(100), width=72))
```
```
100% |##################################################################|
California with her hands upon it five little dried orange pips in the
name of the man who had done their work. When I went and saw him last he
smoothed one out, I am afraid that I found waiting for me was more a
feeling of impending misfortune impressed me neither favourably nor the
reverse. She hurried from the wedding? Yes, there came a neat little
'Hosmer Angel' at the rocket, fitted with a wooden leg? Something like
fear sprang up in the most incisive reasoner and most energetic agent in
Europe.
```

## Save and restore models

The models can be saved and restored using cPickle:
```
import cPickle as pickle

with open('dctc.p', 'wb') as fp:
    pickle.dump(mc.dct, fp)
with open('dctc.p', 'rb') as fp:
    mc.dct = pickle.load(fp)
```

