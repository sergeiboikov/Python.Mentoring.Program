def myzip(*args):
    iterators = [iter(arg) for arg in args]
    iterators_count = len(iterators)
    result = []
    while iterators_count >= 0:
        for it in iterators:
            try:
                elem = next(it)
                result.append(elem)
                yield elem
            except StopIteration:
                iterators_count -= 1


print(list(myzip(['A', 'B', 'C'], [1, 2, 3])))
print(list(myzip('!', ['A', 'B', 'C', 'D'], range(1, 3))))
