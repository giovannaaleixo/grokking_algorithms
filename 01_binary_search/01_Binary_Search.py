# Binary Search

def binary_search(lista, item):
    low = 0
    high = len(lista) -1
    
    while low <= high:
        middle = (low + high) // 2
        tentative = lista[middle]
        
        if tentative == item:
            return middle
        if tentative > item:
            high = middle - 1
        else:
            low = middle + 1
            
    return None

my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 1)) #return the position of the number
print(binary_search(my_list, -1)) #None