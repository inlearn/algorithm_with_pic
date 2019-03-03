
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    bench = arr[0]
    low = []
    high = []
    for item in arr[1:]:
        if item < bench:
            low.append(item)
        else:
            high.append(item)
    return quicksort(low) + [bench] + quicksort(high)


import random


def quicksortrand(arr):  # 最糟是bench为最小的值 O(n*n)如果每次随机选择一个bench,那么平均与最好都是O(nlogn)
    if len(arr) <= 1:
        return arr
    rand_index = random.randrange(0, len(arr) - 1)
    bench = arr[rand_index]
    low = []
    high = []
    for item in [j for i, j in enumerate(arr) if i != rand_index]:
        if item < bench:
            low.append(item)
        else:
            high.append(item)
    return quicksort(low) + [bench] + quicksort(high)


if __name__ == "__main__":
    print(quicksort([10, 5, 2, 3]))
    print(quicksortrand([10, 5, 2, 3]))