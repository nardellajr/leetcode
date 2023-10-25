# 2011 - Final Value of Variable After Performing Operations

def finalValueAfterOperations(operations):
    x = 0
    for i in operations:
        if i == "--X" or i == "X--":
            x -= 1
        else:
            x += 1

    return x


# time complexity: O(n), space complexity: O(1)
def generator_finalValueAfterOperations(operations):
    return sum(1 if i == "++X" or i == "X++" else -1 for i in operations)


if __name__ == "__main__":
    # operations = ["++X", "++X", "X++"]
    operations = ["--X", "X++", "X++"]
    # operations = ["X++", "++X", "--X", "X--"]
    print(finalValueAfterOperations(operations))

    print(generator_finalValueAfterOperations(operations))
