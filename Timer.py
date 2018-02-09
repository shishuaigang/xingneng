import functools
import timeit


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('开始执行%s' % (func.__name__,))
        bg_time = timeit.default_timer()
        func(*args, **kwargs)
        end_time = timeit.default_timer()
        re = end_time - bg_time
        print('执行完%s花费了%.2fs' % (func.__name__, re))

    return wrapper
