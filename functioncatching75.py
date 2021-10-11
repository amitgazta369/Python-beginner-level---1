import time
from functools import lru_cache

@lru_cache(maxsize=32)
def some_work(n):
    time.sleep(n)
    return n
if __name__ =='__main__':
    print("now running some work")
    some_work(3)
    some_work(5)
    some_work(7)
    some_work(8)
    some_work(9)
    print("done... calling again")
    some_work(3)
    print("called again")
