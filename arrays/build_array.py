import time


def buildArray(nums: list[int]) -> list[int]:
    results = []
    for x in range(len(nums)):
        results.append(nums[nums[x]])
    return results


# shorter, but not faster than loop above
def buildArray_2(nums: list[int]) -> list[int]:
    return [nums[i] for i in nums]


def test_results(results: list[int], expected: list[int]):
    if results == expected:
        print('Passed')
    else:
        print('Failed')
        print(f' my value: ', r, 'Expected value: ', expected)


if __name__ == '__main__':

    nums1 = [0, 2, 1, 5, 3, 4]
    expected = [0, 1, 2, 4, 5, 3]
    begin = time.perf_counter()
    r = buildArray(nums1)
    test_results(r, expected)
    print(f"time: ", time.perf_counter() - begin)

    nums1 = [0, 2, 1, 5, 3, 4]
    expected = [0, 1, 2, 4, 5, 3]
    begin = time.perf_counter()
    r = buildArray_2(nums1)
    test_results(r, expected)
    print(f"time: ", time.perf_counter() - begin)

