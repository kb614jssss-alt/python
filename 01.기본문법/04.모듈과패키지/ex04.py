from travel import thailand             #모듈의 위치찾기
from travel.vietnam import *

thailand.thailand2()
vietnam1()

import inspect
import random

print(1, inspect.getfile(random))
print(2, inspect.getfile(thailand))