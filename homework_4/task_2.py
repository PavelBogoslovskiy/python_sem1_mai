import itertools

######### 1
try:
    print('№ 1')
    # бесконечный генератор, начиная с 1 и с шагом 1
    infinite_generator = itertools.count(1)
    # первые 5 штук
    for _ in range(5):
        print(next(infinite_generator))
except StopIteration:
    print("Итератор пуст")


######### 2
numbers = iter([1, 2, 3])

try:
    # возводим в степень 2
    powered_numbers = itertools.starmap(pow, [(num, 2) for num in numbers])
    print('№ 2')
    print(list(powered_numbers))
except StopIteration:
    print("Итератор пуст")


######### 3
iterator1 = iter([1, 2, 3])
iterator2 = iter([4, 5])
iterator3 = iter([6, 7, 8])

try:
    combined_iterator = itertools.chain(iterator1, iterator2, iterator3)
    print('№3')
    print(list(combined_iterator))
except StopIteration:
    print("Итератор пуст")



