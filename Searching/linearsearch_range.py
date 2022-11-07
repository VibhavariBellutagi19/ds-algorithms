def linear_search(arr, target, start, end):
    if len(arr) == 0:
        return -1

    for i in range(start, end + 1):
        if arr[i] == target:
            return i
    return -1

def main():
    arr = [10,13,14,15,8,19]
    target = 15
    start = 1
    end = 3

    result = linear_search(arr, target, start, end)
    if result == -1:
        print(" Element not found")
    else:
        print(" Element found: {}".format(result))


if __name__ == "__main__":
        main()