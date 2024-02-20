array = [3,4,5,6,7]
@staticmethod
def bubble_sorted():
    n = len(array)
    for i in range(n-1):
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1] , array[j]
        print(array)


bubble_sorted()