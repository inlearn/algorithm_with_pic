def binary_search(a_list, item):
    '''
    :param a_list:
    :param item:
    :return: place int
    '''
    low = 0
    high = len(a_list) - 1

    while low <= high:
        mid = (high + low) // 2
        if item == a_list[mid]:
            return mid
        if item > mid:
            low = mid + 1
        else:
            high = mid - 1
    return None


if __name__ == "__main__":
    print(binary_search([1, 4, 6, 7], 9))
