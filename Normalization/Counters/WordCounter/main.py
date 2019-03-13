
from preprocess import make_tokens
from collections import Counter
import string
import operator
import csv
import chardet
import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from tqdm import tqdm



objects = []
performance = []

with open('RESULT.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    
    count_all = Counter()

    for line in tqdm(reader):
        tweet = line['text']
        terms_single = set(make_tokens(tweet))
        print(terms_single)
        count_all.update(terms_single)

    for tag, count in count_all.most_common(20):
       
        if len(tag) > 2:
            objects.append(tag)
            performance.append(count)

y_pos = np.arange(len(objects))

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Quantidade')
plt.title('hashtags')
plt.show()
