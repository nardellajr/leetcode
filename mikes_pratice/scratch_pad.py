# test python logic


def test():

    n = 4
    index = 2
    # this loop moves the values in the list to the right
    # array length is n, index is the position to insert
    #                (4 - 1, 2, -1)
    for i in range(n - 1, index, -1):
        print(i)  # 3, 2, 1
        # target[i] = target[i - 1]



if __name__ == '__main__':
    test()