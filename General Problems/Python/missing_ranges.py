def find_missing_ranges(list_with_missing_elements: list) -> list:
    if len(list_with_missing_elements) == 0:
        missing_ranges = list()
    elif len(list_with_missing_elements) == 100:
        missing_ranges = list(range(100))
    else:
        missing_ranges = list()

        first = False
        for element in list_with_missing_elements:
            if not first:
                previous_element = element
                first = True
            else:
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
    given_list = [0, 1, 3, 50, 75]
    print(find_missing_ranges(given_list))
