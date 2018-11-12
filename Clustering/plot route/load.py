import json
import randomcolor


def resultgeo_Json():

    todo = []
    rand_color = randomcolor.RandomColor()
    colors = rand_color.generate(hue="random", count = 717)
    cor = 0
    for line in open("CLUSTER.json"):
        data = json.loads(line)
        todo.append([data['geos'], colors[cor]])
        cor += 1
    return todo
