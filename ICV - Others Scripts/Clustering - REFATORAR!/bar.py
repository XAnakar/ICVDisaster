# Print iterations progress


def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
 
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')

    # Print New Line on Complete

    if iteration == total: 
        print()

'''
from time import sleep
import csv

Indentificares = [
    data['id_str'] for data in csv.DictReader(open("formated.csv","r"))
]

items = list(Indentificares)
l = len(items)

printProgressBar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50)

for i, item in enumerate(items):
    print(item)
    printProgressBar(i + 1, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
'''