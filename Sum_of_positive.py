def positive_sum(arr):
    n=0
    for x in range(len(arr)):
        if arr[x]>0:
            n+=arr[x]
    return n