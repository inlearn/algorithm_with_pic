def countdown(i):
    print(i)
    if i <= 0:
        return
    else:
        countdown(i - 1)


def mysum(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + mysum(arr[1:])


if __name__ == "__main__":
    # countdown(5)
    print(mysum([1, 3, 4]))
