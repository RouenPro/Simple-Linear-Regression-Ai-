import numpy as np
from timeit import timeit

np.random.seed(444)
x = np.random.choice([False, True], size=100000)


def count_transitions(x) -> int:
    count = 0
    for i, j in zip(x[:-1], x[1:]):
        if j and not i:
            count += 1
    return count


print(count_transitions(x))
print(np.count_nonzero(x[:-1] < x[1:]))

setup = 'from __main__ import count_transitions, x; import numpy as np'
num = 1000
t1 = timeit('count_transitions(x)', setup=setup, number=num)
t2 = timeit('np.count_nonzero(x[:-1] < x[1:])', setup=setup, number=num)
print('Speed difference: {:0.1f}x'.format(t1 / t2))

