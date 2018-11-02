from preprocess import preprocess
from collections import Counter
import string
import operator
import json
import chardet
import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from tqdm import tqdm


objects = []
performance = []

with open('RESULT.json', 'r') as f:

    count_all = Counter()
    for line in tqdm(f):
        tweet = json.loads(line)
        terms_single = set(
            [
                term for term in preprocess(tweet['text'])
            ]
        )
        terms_hash = [
            term.lower() for term in preprocess(tweet['text'])
            if term.startswith('#')
        ]
        count_all.update(terms_hash)

    for tag, count in count_all.most_common(50):

        print(tag, count)
        objects.append(tag)
        performance.append(count)


y_pos = np.arange(len(objects))

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Quantidade')
plt.title('hashtags')
plt.show()
