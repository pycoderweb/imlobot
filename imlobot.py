from uzwords import words
import cyrtranslit
from difflib import get_close_matches

wordsuz = []
for suz in words:

    wordsuz.append(cyrtranslit.to_latin(suz))

def checkword(word):
    word = word.lower()

    matches = set(get_close_matches(word,words))

    aviable = False

    if word in matches:
        aviable = True
        matches = word

    return {'aviable':aviable, 'matches':matches}

def chekworduz(word):
    word = word.lower()

    matches = set(get_close_matches(word, wordsuz))

    aviable = False

    if word in matches:
        aviable = True
        matches = word

    return {'aviable': aviable, 'matches': matches}




