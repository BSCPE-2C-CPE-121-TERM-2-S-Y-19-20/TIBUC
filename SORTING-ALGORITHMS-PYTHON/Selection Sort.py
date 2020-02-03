A= [20, 16, 5,9, 2, 12, 4, 10]
print(A)
for i in range(len(A)):
    min_idx=i

    for j in range(i+1, len(A)):
        if A[min_idx]>A[j]:
            min_idx=j

    A[i], A[min_idx]=A[min_idx], A[i]
print ("Sorted Array")
for i in range(len(A)):
    print("%d" %A[i])
