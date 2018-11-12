import json

bag_of_words = [line.lower().replace("\n", "") for line in open('base.txt')]
bag_of_words.sort()


def classificador(arraytext, bag):

    for index in arraytext:
        for line in bag:
            if line.lower() == index.lower(): # Aqui seleciona as ocorrências de palavras do "base.txt"
                print(line)
                return True
    return False


count = 0
for line in open('CLUSTER.json'):
    data = json.loads(line)

    if classificador(data['texts'], bag_of_words):
        count += 1

print("Resultado: ", count)
