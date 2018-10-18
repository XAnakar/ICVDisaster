import json

geos = [json.loads(line)['geos'] for line in open('Clusters.json')]
geos[0].sort
print(geos[0])