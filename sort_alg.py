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

def bubble_sort(arr):
    for n in range(1,len(arr)): # iterate through the entire array
        for j in range(1,len(arr)-n-1): # won't bother sorted items that are already sorted
            if arr[j] > arr[j+1]: # sort such that lower value come before higher values
                arr[j],arr[j+1]=arr[j+1],arr[j] # classic var reassignment
    return arr

# sample array
# we need three variables to deal with - username, date, and score
# the arrays should be in format --> high_scores = [('','10-12-1986',450),('','',743),('','',321)]

from time import localtime

def retrieve_time():
    return f"{localtime()[0]}-{localtime()[1]}-{localtime()[2]}"

sample_array = [("Oxford", "90-32-1239", 3244),("Bob", "32-11-1890", 34553),("Andrew", "10-22-2929", 654)]

# def modif_bubble(arr):
#     for n in range(1, len(arr)):
#         for j in range(1,len(arr)-n-1):
#             if arr[j][2] > arr[j+1][2]:
#                 arr[j],arr[j+1]=arr[j+1],arr[j] 
#     return arr

def modif_bubble(arr):
    for n in range(1, len(arr)):
        for j in range(1,len(arr)-n-1):
            if arr[j][2] > arr[j+1][2]:
                hold = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = hold
                print('fuck you')
    return arr

print(modif_bubble(sample_array))