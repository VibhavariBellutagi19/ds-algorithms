# Binary Search

## Tricks: 

### Binary search in short
```
- find the middle element
-  target > mid => right else left
-  middle == target => element found
```

### Moutain array
```
- if the e[mid] > e[mid+1] -> decreasing part of array
- if the e[mid] < e[mid+1] -> ascending part of array
- At the end, start == end and can return start or end
- Loop breaking condition would be start < end ( not s <= e )
```

### Search in Rotated Sorted Array without duplicates
```
- if the pivot
    - if arr[mid] > arr[mid - 1] then pivot index is mid
    - if arr[mid] < arr[mid - 1] then pivot index is mid-1
    - if arr[mid] <= arr[start] then search from end = mid - 1
    - elif arr[mid] > arr[start] then search from start = mid + 1
- Binary search from start to pivot - 1
- Otherwise Binary search from pivot + 1 to end
```
### Search in Rotated Sorted Array without duplicates
```
- if the pivot
    - if arr[mid] > arr[mid - 1] then pivot index is mid
    - if arr[mid] < arr[mid - 1] then pivot index is mid-1
    - if arr[mid] == arr[start] and arr[mid] == mid, skip these duplicates ( start ++ and end --)
    - if arr[start] < arr[mid] or (arr[start] == arr[mid] and arr[mid] > arr[end]) => start = mid + 1
    - else end = mid - 1
- Binary search from start to pivot - 1
- Otherwise Binary search from pivot + 1 to end
```

### Rotation Count in Rotated Sorted array
```
Simple trick - rotation count would be pivot times + 1
```

### smallest element in array which is >= target

### biggest element in array which is <= target

### find-first-and-last-position-of-element-in-sorted-array