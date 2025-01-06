from numpy import random
import time

x = random.rand(3, 5)
def zero_to_infinity():
    i = 0
    while True:
        yield i
        i += 1

for y in zero_to_infinity():
    print(time.strftime("%a, %d %b %Y %H:%M:%S"))
    print(x)
    time.sleep(60)
