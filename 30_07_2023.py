#Implement Binary Search

def bsr(x,value,l,h):
    if l>h:
        return "value not found"
    m = (l+h)//2
    mid_value = x[m]

    if mid_value == value:
        return m
    
    if mid_value < value:
        l = m+1
    else:
        h = m-1
    return bsr(x,value,l,h)


x = [1,23,45, 75,878,3432,2323,4,5,66,9]
print(bsr(x,1000,0,len(x)-1))
    
#Implement Merge Sort


def marge(x,l,m,r):
    n1 = m-l+1
    n2 = r-m

    L = []
    R = []
    print(n1)

    for i in range(0,n1):
        L.append(x[l+i])

    for j in range(0,n2):
        R.append(x[m+1+j])

    i = 0 # for l side
    j = 0 # for r side
    k = l # for merged one

    while i < n1 and j < n2 :
        if L[i] <= R[j]:
            x[k] = L[i]
            i += 1
        else :
            x[k] = R[j]
            j += 1
        k+=1
    
    while i<n1:
        x[k] = L[i]
        i+=1
        k+=1

    while j<n2:
        x[k] = R[j]
        j+=1
        k+=1

def margesort(x,l,r):
    if l<r:
        m= l+(r-l)//2
        margesort(x,l,m)
        margesort(x,m+1,r)
        marge(x,l,m,r)

arr = [12,34,2,98,46,19,45,54,32,74,15,34]
margesort(arr,0,len(arr)-1)
print(arr)


#Implement Quick Sort

def quicksort(x):
    if len(x) <= 1:
        return(x)
    else:
        p = x[0]
        l = [i for i in x[1:] if i < p]
        r = [i for i in x[1:] if i >= p]
        return quicksort(l) + [p] + quicksort(r)
    
arr = [4,3,2,1,2,5,6,74,4]
sorted_array = quicksort(arr)
print(sorted_array)



#Implement Insertion Sort


def insertionSort(arr):
 
    
    for i in range(1, len(arr)):
 
        key = arr[i]
 
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
 
arr = [31,12,1996,26,7,1997]
insertionSort(arr)
for i in range(len(arr)):
    print ("% d" % arr[i])
 



#Write a program to sort list of strings (similar to that of dictionary)

def dict_sort_key(string):
    return tuple(ord(c) for c in string)

def sort_list_as_dictionary(input_list):
    return sorted(input_list, key=dict_sort_key)

input_list = ["apple", "orange", "banana", "grape"]
sorted_list = sort_list_as_dictionary(input_list)
print(sorted_list)
