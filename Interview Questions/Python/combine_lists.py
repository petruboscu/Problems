def combine_lists(lists: list) -> list:
    combined_list = []
    combined_list_element = []
    number_of_lists = len(lists)
    max_length = None
    for list_index in range(number_of_lists - 1):
        max_length = max(len(lists[list_index]), len(lists[list_index + 1]))
    for list_element_index in range(max_length):
        for list_index in range(number_of_lists):
            if list_element_index < len(lists[list_index]):
                combined_list_element.append(lists[list_index][list_element_index])
            else:
                combined_list_element.append(None)
        combined_list.append(combined_list_element)
        combined_list_element = []
    return combined_list


if __name__ == '__main__':
    first_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    second_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    third_list = ['!', '@', '#', "$", '%', '^', '&', '*', '(', ')', '_']
    forth_list = ['-', '+', ':', 'X', '<', '>', '=', '<=', '>=']

    list_to_be_combined = [first_list, second_list, third_list, forth_list]

    for element in combine_lists(list_to_be_combined):
        print(element)
