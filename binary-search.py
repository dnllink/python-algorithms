numbers = range(1, 10000)
guess = 30000

def binary_search(list, number_to_find):
    min_index = 0
    max_index = len(list) - 1

    while min_index <= max_index:
        half_index = int((min_index + max_index) / 2)
        if list[half_index] == number_to_find:
            return half_index
        elif list[half_index] > number_to_find:
            max_index = half_index - 1
        elif list[half_index] < number_to_find:
            min_index = half_index + 1
    return -1


def get_max_index(list):
    max_value = 0
    max_index = 0
    for i in range(0, len(list)):
        if list[i] > max_value:
            max_value = list[i]
            max_index = i
    return max_index

def selection_sort(list):
    print(list)
    for i in range(0, len(list)):
        max_index = get_max_index(list[i:len(list)])
        actual_value = list[i]
        max_value = list[max_index + i]
        list[i] = max_value
        list[max_index + i] = actual_value
    print(list)

        
selection_sort([3,1,9,4,7,21,0,2,8,6,19])
print(binary_search([1,3,5,7,9,11,13,15], 5)) # 2
print(binary_search([1,3,5,7,9,11,13,15], 13)) # 6
print(binary_search([1,3,5,7,9,11,13,15], 12)) # -1