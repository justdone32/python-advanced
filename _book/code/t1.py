import time
 
def time_me(fn):
    def _wrapper(*args, **kwargs):
        start = time.clock()
        fn(*args, **kwargs)
        print("%s cost %s second"%(fn.__name__, time.clock() - start))
    return _wrapper
 
@time_me
def test(x, y):
    time.sleep(0.1)
 
@time_me
def test2(x):
    time.sleep(0.2)
 
test(1, 2)
test2(2)