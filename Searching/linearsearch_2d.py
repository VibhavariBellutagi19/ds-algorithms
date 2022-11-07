# Introduction: 
# Problem Statement: find the element in 2d array using linear search
# Input: arr = 18,12,-7,3,14,28
# Output: 
# Time complexity: O(n^2)

def search_in_2D(arr,target):
    for row in range(len(arr)):
        for col in range(len(arr[row])):
            if arr[row][col] == target:
                return ans.append([row,col])
    ans[0][0] = -1,-1
    return ans

def main():
    arr = [
        [1,2,3,4],
        [4,1,23,31],
        [43,56,78,12]
        ]
    target = 56
    print(search_in_2D(arr,target))


if __name__ == "__main__":
        main()