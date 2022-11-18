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

### smallest element in array which is >= target

### biggest element in array which is <= target

### find-first-and-last-position-of-element-in-sorted-array