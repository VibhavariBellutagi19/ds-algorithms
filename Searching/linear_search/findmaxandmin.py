# Introduction: 
# Problem Statement: find min and max from array 
# Input: 
# Output: 
# Time complexity: 

def find_min(arr):
    min_num = arr[0]
    for i in arr:
        if min_num < i:
            min_num = i
    return min_num

def find_max(arr):
    max_num = arr[0]
    for i in arr:
        if max_num > i:
            max_num = i
    return max_num

def main():
    arr = [18,12,-7,3,14,28]

    print("Min number in the element - {}".format(find_min(arr)))
    print("Max number in the element - {}".format(find_max(arr)))



if __name__ == "__main__":
        main()