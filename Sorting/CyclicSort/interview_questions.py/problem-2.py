# Introduction: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
# tricks:
# Output: 
# Input:
# Time complexity:

def cyclic_sort(arr):
    n = len(arr)
    i = 0

    while(i < n):
        correct = arr[i] - 1
        if(arr[i] != arr[correct]):
            arr[i], arr[correct] = arr[correct], arr[i]
        else:
            i += 1
    return arr

def findDisappearedNumbers(arr):
    missing_numbers = []
    for i in range(len(arr)):
        if i != arr[i] - 1:
            missing_numbers.append(i + 1)
        else:
            i += 1
    return missing_numbers
        

def main():
    arr = [1,1]

    print("Array before sorting: {}".format(arr))
    cyclic_sort(arr)
    print("Array before sorting: {}".format(arr))

    disappearedNumber = findDisappearedNumbers(arr)

    print("missing numbers: {}".format(disappearedNumber))

if __name__ == "__main__":
    main()