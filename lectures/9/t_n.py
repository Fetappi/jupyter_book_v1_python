from time import perf_counter
from random import uniform
import numpy as np


N = 10_000_000

# Создаём списки случайных чисел
a = [uniform(-1, 1) for i in range(N)] # новый синтаксис, список случайных чисел
b = [uniform(-1, 1) for i in range(N)]
c = [0.] * N 

a_n = np.asarray(a)
b_n = np.asarray(b)
c_n = np.asarray(c)
# Измеряем время сложения этих списков
t1 = perf_counter()

c_n = a_n + b_n
		
t2 = perf_counter()
print(f"{(t2 - t1) * 1000} ms") # perf_counter() - время в секундах