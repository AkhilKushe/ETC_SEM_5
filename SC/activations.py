def bi_threshold(val):
    def func(x):
        if x >= val:
            return 1
        else:
            return -1
    return func
    
def threshold(val):
    def func(x):
        if x >= val:
            return 1
        else:
            return 0
    return func


def sign(x): 
    if x >= 0:
        return 1
    else:
        return -1
