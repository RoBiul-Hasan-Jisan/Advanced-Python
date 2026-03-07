# Decorator to Log Function Call Time

import time

def log_time(func):
    """ Decorator to log func calling """
    def show(*args,**kwargs):
        print(f"Funtion'{func.__name__}' call at {time.strftime('%X')} ")
        re = func(*args,**kwargs)
        return re
    return show

@log_time


def gt(name):
    print(f"hello,{name}!")

gt("Alice")

