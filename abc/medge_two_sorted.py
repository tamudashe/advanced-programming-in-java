# O(m*n) wost case time complexity, when all the elements in array1 are greater that elements in array2
# O(1) space
def medge_sorted_arrays(array1, array2):
    m, n = len(array1), len(array2)

    # iterate through all elements of array2 starting from the last element
    for i in range(n-1, -1, -1):
        # find the smallest element greater than array2[i] 
        # move all elements one position ahead till the smallest greater element
        last = array1[m - 1]
        j = m - 2
        while (j >= 0 and array1[j] > array2[i]):
            array1[j+1] = array1[j]
            j -= 1

        # if there was a greater element
        if (j != m - 2 or last > array2[i]):
            array1[j+1], array2[i] = array2[i], last


if __name__ == '__main__':
    array1 = [1, 3, 4, 6, 8, 30]
    array2 = [5, 7, 9, 10]
    print(array1, '---', array2)
    medge_sorted_arrays(array1, array2)
    print(array1, '---', array2)
