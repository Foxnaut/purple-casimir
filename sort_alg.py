def modif_bubble(arr):
    for n in range(0, len(arr)):
        for j in range(0,len(arr)-n-1):
            if arr[j][2] > arr[j+1][2]:
                arr[j],arr[j+1]=arr[j+1],arr[j] 
    return arr
