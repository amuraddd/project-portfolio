"""
Quick Sort:
Quick Sort requires the input array to be partitioned around a pivot element.
=============================================================================
Partitioning requires an invariant where you keep track of two boundaries:
    i:= all elements between the pivot and i are less than the pivot
    j:= all elements between i and j are greater than the pivot
As you process through the array you swap elements when this invariant does not hold.
E.g. you have an array [3,8,2,5,1,4,7,6], using 3 to be the pivot on the first increment [i] and 3 are properly
placed and [i] and [j] have 8 which is greater than 3. On the second increment between the pivot and [i] you have 8 which
is not less than 3 and between [i] and [j] you have 2 which is not greater than 3(3 being the pivot), this is where
you swap 8 and 2. After the swap the invariant holds again and you continue the same approach until the entire array is 
processed. At the very end you replace the pivot with the last element in the array which is less than the pivot. 
Increment i and i both when a swap occurs to change the boundary. Only increment j when no swap occurs.
=============================================================================

l: leftmost index
r: rightmost index

Invariant:
i and j are boundaries to seperate smaller from pivot and larger from pivot elements in the unsorted array. Between the pivot and i all elements are smaller than the pivot.
Keeping this under consideration the partition function seperates the smaller and larger integers and places the pivot at the correct sorted location. The quickSort function 
recurses on the left and the right side of this partitioned array until the base case is reached.

- In the case below we use the first element as the pivot.
"""
def data(fileName):
    unsorted = open(fileName, 'r')
    unsortedList = [int(i.rstrip()) for i in unsorted] #remove blank lines from the data and convert strings to a list of integers.
    return unsortedList

def partition(array, l): #l refers to the leftmost index
    pivot = array[l] #first element as the pivot
    #i and j both start at the same location
    i = l + 1 #left pointer
    for j in range(l+1, len(array)): #
        if array[j] < pivot: 
            (array[j],array[i]) = (array[i], array[j]) #between array[i] and array[j] everything should be less than the pivot. If not then swap.
            i += 1
    #place the pivot at the right place
    (array[l], array[i-1]) = (array[i-1], array[l])
    return i-1

def quickSort(array, l, r):
    if len(array) == 1:
        return array
    
    if l < r:
        newPivot = partition(array, l) 
        quickSort(array, l, newPivot-1)
        quickSort(array, newPivot+1, r)

def main(fileName):
    finalList = data(fileName)
    quickSort(finalList, 0, len(finalList))
    print(finalList)
    

if __name__ == '__main__':
    main('QuickSort.txt')