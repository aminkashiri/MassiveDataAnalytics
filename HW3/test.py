import numpy as np
from time import time
# def yield_func():
#     b = [1,2,3]
#     a = [9,8,7]
#     for x in a:
#         yield from b
#         yield x

# a = np.fromiter(yield_func(), dtype=int).reshape(4,3)

# print(a)
# b = np.array([
#     [0,1],
#     [0,2]
# ])

# print(a[:, b].shape)



# obj = yield_func()
# for i in range(12):
#     print(next(obj))


# a = np.array([
#     [1,4],
#     [3,2],
#     [3,1]])

# print(a)
# print(a.flatten())
# print(np.unique(a.flatten()))

# a = {
#     1 : 'amin'
# }
# print(a[1])




# import sys
# a = [True,True,True]
# print(sys.getsizeof(a))

# temp = time()
# a = [12,3,5,7]
# for i in range(100):
#     a.append(1)
# print(time()-temp)

# temp = time()
# a = np.array([12,3,5,7])
# for i in range(100):
#    a = np.append(a,1 )
# print(time()-temp)


a = [1,5,35,7,87548,68,3,6,73,6,7,6,3,73,57,64732648,8,3,82,298147,107,5703579,356,92956926,959,652,9672597,27502,57920567,957205,9675275,9735070,22476,859,729569,207,927,959,7027]
b = (1,3,82,652)
c = {5436534,46,53,7,73,5,784,27,5726725,72,7,5,35,652,6}

temp = time()
for i in range(100):
    d =  all(candidate_item in a for candidate_item in b)
    e =  all(candidate_item in a for candidate_item in c)
print(time()-temp)

temp = time()
for i in range(100):
    d = set(b) <= set(a)
    e = set(c) <= set(a)
print(time()-temp)

temp = time()
for i in range(100):
    d = set(b).issubset(set(a))
    e = set(c).issubset(set(a))
print(time()-temp)

# temp = time()
# for i in range(100):
#     d = list(b) <= a
#     e = list(c) <= a
# print(time()-temp)

# print([1,2] <= [1,2,3])
# print((1,2) <= (1,2,3))

# temp = time()
# for i in range(10000):
#     a = 1 < 2
# print(time()-temp)
# temp = time()
# for i in range(10000):
#     a = 1.9 < 2.4
# print(time()-temp)

# lambda x: all(candidate_item in x[1] for candidate_item in x[0])