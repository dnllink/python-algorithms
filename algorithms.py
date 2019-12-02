def recursive_sum(numbers):
    if len(numbers) == 0:
        return 0
    elif len(numbers) == 1:
        return numbers[0]
    else:
        return numbers[0] + sum(numbers[1:len(numbers)])


def recursive_count_items(numbers):
    if len(numbers) == 0:
        return 0
    elif len(numbers) == 1:
        return 1
    else:
        return 1 + recursive_count_items(numbers[1:len(numbers)])


def recursive_max_value(numbers):
    if len(numbers) == 0:
        return 0
    elif len(numbers) == 1:
        return numbers[0]
    else:
        max_value = recursive_max_value(numbers[1:len(numbers)])
        if numbers[0] >= max_value:
            return numbers[0]
        else:
            return max_value


def recursive_quick_sort(numbers):
    if len(numbers) < 2:
        return numbers
    pivot_index = int(len(numbers)/2)
    pivot = numbers[pivot_index]
    less_than_pivot = []
    more_than_pivot = []
    for i in range(0, len(numbers)):
        if numbers[i] < pivot:
            less_than_pivot.append(numbers[i])
        elif numbers[i] > pivot:
            more_than_pivot.append(numbers[i])
    return recursive_quick_sort(less_than_pivot) + [pivot] + recursive_quick_sort(more_than_pivot)


print(recursive_quick_sort([99, 88, 77, 55, 66, 33, 44, 22]))
