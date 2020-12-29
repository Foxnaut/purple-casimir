sample_array = [("john", 568, "date"), ("abigail", 45, "date"), ("jeff", 87, "date")]

l = [9,8,2,10,4,5,7] 

# here's the insertion sort

def ins_sort(arr):

# we loop through the array

    for n in range(1, len(arr)):
        # the key is just the value of the array at any point
        key = arr[n]

        # k is the index of the item before the element
        k = n-1

        while k >= 0 and key < arr[k]: # k can't be less than one, since the arr
            arr[k+1] = arr[k]
            k -= 1
        arr[k+1] = key
        # if arr[n] < arr[n-1]:
        #     arr[n], arr[n-1] = arr[n-1], arr[n]


ins_sort(l)