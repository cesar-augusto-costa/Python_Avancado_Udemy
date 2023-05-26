# count é um iterador sem fim (itertools)
# INFINITO

from itertools import count

count1 = count()
count2 = count(8, 8)
count2 = count(step=8, start=8)
range1 = range(2, 10, 2)

print(next(count1))
print(next(count1))
print(next(count1))

print('count __iter__:', hasattr(count1, '__iter__'))
print('count __next__:', hasattr(count1, '__next__'))
print('range __iter__:', hasattr(range1, '__iter__'))
print('range __next__:', hasattr(range1, '__next__'))

print('count')
for i in count2:
    if i >= 20:
        break
    print(i)
print()
