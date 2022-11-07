# Introduction: 
# Problem Statement: Linear searching iterating through the loop.
# Input: 
# Output:  

def linear_search(arr,target):
    if len(arr) == 0:
        return -1

    for i in range(0, len(arr)):
        if arr[i] == target:
            return i
    return -1

def main(): 
    arr = [10,13,14,15,8,19]
    target = 19

    result = linear_search(arr, target)
    if result == -1:
        print(" Element not found")
    else:
        print(" Element found at position: {}".format(result))

if __name__ == "__main__":
    main()
