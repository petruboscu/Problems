def find_missing_ranges(list_with_missing_elements: list) -> list:

    missing_ranges = list()

    if len(list_with_missing_elements) == 0:
        missing_ranges.append('0 -> 99')

    elif len(list_with_missing_elements) == 100:
        missing_ranges.append(None)

    else:
        missing_ranges = list()

        previous_element = list_with_missing_elements[0]
        if previous_element != 0:
            missing_ranges.append(f'0 -> {previous_element - 1}')
        for element in list_with_missing_elements[1:]:
            if element - previous_element == 2:
                missing_ranges.append(f'{element - 1}')
            elif element - previous_element > 2:
                missing_ranges.append(
                    f'{previous_element + 1} -> {element - 1}')
            previous_element = element
        if previous_element != 99:
            missing_ranges.append(f'{previous_element + 1} -> 99')

    return missing_ranges


if __name__ == '__main__':
    first_list = [0, 1, 3, 50, 75]
    print(find_missing_ranges(first_list))

    second_list = list()
    print(find_missing_ranges(second_list))

    third_list = list(range(100))
    print(find_missing_ranges(third_list))
