import random
from datetime import datetime as dt
random.seed(dt.now())
for i in range(5):
    print(random.randint(0,10),end=" ")