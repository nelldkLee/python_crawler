
it = map(lambda x: print(x, end=' '), [1, 2, 3, 4])
next(it)
next(it)
next(it)
next(it)
print()
lst = list(map(lambda x: x**2, [1, 2, 3, 4]))


lst = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4]))
print(lst)


asd = map(1,'test')
