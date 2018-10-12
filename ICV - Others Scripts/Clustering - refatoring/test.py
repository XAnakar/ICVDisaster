import time
from tqdm import tqdm

for index in tqdm(range(100)):
    print(index)
    time.sleep(0.1)
    