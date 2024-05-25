def merge_sort(elements, reversed=False):
    """
    Sorts a list of integers using the merge sort algorithm.

    Args:
        elements (list): The list of integers to be sorted.
        reversed (bool, optional): A boolean indicating whether to sort in ascending (False) or descending (True) order. Defaults to False.

    Returns:
        list: The sorted list.
    """
    # Base case: If there is only one element, return it as it is already sorted.
    if len(elements) <= 1:
        return elements
    mid = len(elements) // 2
    # Recursively sort the left and right halves.
    left_half = merge_sort(elements[:mid], reversed)
    right_half = merge_sort(elements[mid:], reversed)
    # Merge the sorted left and right halves.
    return merge(left_half, right_half, reversed)

def merge(left, right, reversed):
    """
    Merges two sorted lists into one sorted list.

    Args:
        left (list): The first sorted list.
        right (list): The second sorted list.
        reversed (bool): A boolean indicating whether to sort in ascending (False) or descending (True) order.

    Returns:
        list: The merged sorted list.
    """
    merged = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if reversed:
            # If sorting in descending order, compare elements in reverse.
            if left[left_index] >= right[right_index]:
                merged.append(left[left_index])
                left_index += 1
            else:
                merged.append(right[right_index])
                right_index += 1
        else:
            # If sorting in ascending order, compare elements normally.
            if left[left_index] <= right[right_index]:
                merged.append(left[left_index])
                left_index += 1
            else:
                merged.append(right[right_index])
                right_index += 1
    # Append the remaining elements from both lists.
    merged += left[left_index:]
    merged += right[right_index:]
    return merged

def print_list(elements, name):
    """
    Prints a list of integers.

    Args:
        elements (list): The list of integers to be printed.
        name (str): The name to be printed before the list.
    """
    print(name + ": " + ' '.join(str(element) for element in elements))

list = [2, 5, 3, 1, 7, 4, 9, 8, 6, 15, 13, 18, 12, 11, 14, 17, 19, 20, 10, 16]
listLength = 20
orderedList = merge_sort(list)
reversedOrderedList = merge_sort(list, True)
print_list(list, "List")
print_list(orderedList, "Ordered List")
print_list(reversedOrderedList, "Reversed Ordered List")
