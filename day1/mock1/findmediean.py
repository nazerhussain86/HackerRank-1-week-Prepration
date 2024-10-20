def findMedian(arr):
  arr.sort()

 n = len(arr)
 middle = n//2

 if n % 2 != 0:
 return arr[middle]

 else:
 return (arr[middle - 1] + arr[middle]) / 2
