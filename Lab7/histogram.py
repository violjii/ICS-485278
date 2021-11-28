from collections import Counter

import pylab
from matplotlib import pyplot as plt
import numpy as np


def create_text_histogram(text: str):
    counts = Counter(text.replace(" ", ""))
    for i in text:
        plt.bar(i, counts[i])
        plt.savefig('plot.png')
    plt.show()


def create_sentence_histogram(sentence: str):
    symbols = [':', ',', '.', '!', '?']
    for i in range(0, len(symbols)):
        pylab.bar(symbols[i], sentence.count(symbols[i]))
    pylab.show()


create_text_histogram("ssomme ttexxt")
create_sentence_histogram("Hello, world!")
