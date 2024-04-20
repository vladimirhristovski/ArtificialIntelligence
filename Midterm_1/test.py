import math

if __name__ == '__main__':
    test = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
    square = list(test[1])
    index = test.index(tuple(square))

    test[index] = tuple([11,12])

    print(test)

    print(math.ceil(5/2))

    test1 = tuple([(1,1)])
    super =1

    test.remove((7,8))
    print(test)

    print((9,10) in tuple(test))