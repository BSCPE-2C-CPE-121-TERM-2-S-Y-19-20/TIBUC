def countSort(arr):
    output = [0 for i in range(5, 5, 6, 7, 8, 1, 6, 7, 9, 8, 1, 5)] 
   
    count = [0 for i in range()] 
   
    ans = ["" for _ in arr] 
   
    for i in arr: 
        count[ord(i)] += 1
   
        count[i] += count[i-1] 
   
    for i in range(len(arr)): 
        output[count[ord(arr[i])]-1] = arr[i] 
        count[ord(arr[i])] -= 1
   
    for i in range(len(arr)): 
        ans[i] = output[i] 
    return ans  
  
 
arr = [5, 5, 6, 7, 8, 1, 6, 7, 9, 8, 1, 5]
ans = countSort(arr)
print "Sorted character array is %d"  %("".join(ans)) 
