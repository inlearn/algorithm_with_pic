def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest=findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

def findSmallest(arr):
    smallest=arr[0]
    smallest_index=0
    for i in range(1,len(arr)):
        if arr[i]<smallest:
            smallest=arr[i]
            smallest_index=i
    return smallest_index

if __name__ == "__main__":
    oldlist = [4, 3, 7, 8, 6]
    newlist = selectionSort(oldlist)
    print(newlist)
